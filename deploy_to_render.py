#!/usr/bin/env python3
"""
Deploy 5th Corner website to Render.com
Requires: RENDER_API_KEY environment variable
"""
import requests
import os
import sys
import json
import time

RENDER_API_KEY = os.environ.get('RENDER_API_KEY')
RENDER_API_BASE = 'https://api.render.com/v1'

if not RENDER_API_KEY:
    print("❌ Error: RENDER_API_KEY environment variable not set")
    print("\nPlease add your Render API key:")
    print("1. Go to https://dashboard.render.com/u/settings?add-api-key")
    print("2. Click 'Create API Key'")
    print("3. Copy the key")
    print("4. Export it: export RENDER_API_KEY='your-key-here'")
    print("\nOr add it to Cursor Dashboard > Cloud Agents > Secrets")
    sys.exit(1)

headers = {
    'Authorization': f'Bearer {RENDER_API_KEY}',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

def list_services():
    """List all Render services to find existing website"""
    print("🔍 Checking for existing services...")
    response = requests.get(f'{RENDER_API_BASE}/services', headers=headers)
    
    if response.status_code == 401:
        print("❌ Authentication failed. Check your RENDER_API_KEY")
        return None
    
    if response.status_code == 200:
        services = response.json()
        # Look for our website service
        for service in services:
            if 'service' in service:
                svc = service['service']
                name = svc.get('name', '')
                if '5th-corner' in name.lower() or 'raster-website' in name.lower():
                    return svc
    return None

def create_service():
    """Create a new Render web service"""
    print("🚀 Creating new Render service...")
    
    service_data = {
        "type": "web_service",
        "name": "5th-corner-website",
        "autoDeploy": "yes",
        "branch": "main",
        "repo": "https://github.com/mradfo21/5th-corner-web",
        "buildFilter": {
            "paths": [],
            "ignoredPaths": []
        },
        "serviceDetails": {
            "env": "python",
            "buildCommand": "pip install -r requirements.txt",
            "startCommand": "gunicorn app:app",
            "healthCheckPath": "/health",
            "plan": "free",
            "region": "oregon",
            "pullRequestPreviewsEnabled": "no"
        }
    }
    
    response = requests.post(f'{RENDER_API_BASE}/services', 
                           headers=headers, 
                           json=service_data)
    
    if response.status_code in [200, 201]:
        service = response.json()
        return service
    else:
        print(f"❌ Failed to create service: {response.status_code}")
        print(f"Response: {response.text}")
        return None

def set_env_vars(service_id):
    """Set environment variables for the service"""
    print("⚙️  Setting environment variables...")
    
    env_vars = [
        {"key": "FLASK_ENV", "value": "production"},
        {"key": "PYTHON_VERSION", "value": "3.11.0"},
        {"key": "DISCORD_INVITE", "value": "https://discord.gg/Ywk54hKJ5H"},
        {"key": "GAME_API_URL", "value": "https://fiveth-corner-dev-1a00.onrender.com"}
    ]
    
    for env_var in env_vars:
        response = requests.post(
            f'{RENDER_API_BASE}/services/{service_id}/env-vars',
            headers=headers,
            json=env_var
        )
        if response.status_code in [200, 201]:
            print(f"  ✅ Set {env_var['key']}")
        else:
            print(f"  ⚠️  Failed to set {env_var['key']}: {response.status_code}")

def get_service_url(service_id):
    """Get the service URL"""
    response = requests.get(f'{RENDER_API_BASE}/services/{service_id}', headers=headers)
    if response.status_code == 200:
        service = response.json()
        return service.get('service', {}).get('serviceDetails', {}).get('url', '')
    return None

def trigger_deploy(service_id):
    """Trigger a manual deploy"""
    print("🚀 Triggering deployment...")
    response = requests.post(f'{RENDER_API_BASE}/services/{service_id}/deploys', headers=headers)
    
    if response.status_code in [200, 201]:
        deploy = response.json()
        return deploy
    else:
        print(f"❌ Failed to trigger deploy: {response.status_code}")
        return None

def wait_for_deploy(service_id, deploy_id, timeout=600):
    """Wait for deployment to complete"""
    print("⏳ Waiting for deployment to complete...")
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        response = requests.get(
            f'{RENDER_API_BASE}/services/{service_id}/deploys/{deploy_id}',
            headers=headers
        )
        
        if response.status_code == 200:
            deploy = response.json()
            status = deploy.get('deploy', {}).get('status', '')
            
            if status == 'live':
                print("✅ Deployment successful!")
                return True
            elif status in ['build_failed', 'deactivated', 'canceled']:
                print(f"❌ Deployment failed with status: {status}")
                return False
            else:
                print(f"  Status: {status}...")
                time.sleep(10)
        else:
            print(f"⚠️  Error checking deploy status: {response.status_code}")
            time.sleep(10)
    
    print("⏱️  Deployment timeout reached")
    return False

def main():
    print("=" * 60)
    print("5TH CORNER WEBSITE - RENDER DEPLOYMENT")
    print("=" * 60)
    print()
    
    # Check for existing service
    existing_service = list_services()
    
    if existing_service:
        service_id = existing_service.get('id')
        service_name = existing_service.get('name')
        service_url = existing_service.get('serviceDetails', {}).get('url', '')
        
        print(f"✅ Found existing service: {service_name}")
        print(f"   ID: {service_id}")
        print(f"   URL: {service_url}")
        print()
        
        # Trigger a new deploy
        deploy = trigger_deploy(service_id)
        if deploy and 'deploy' in deploy:
            deploy_id = deploy['deploy'].get('id')
            if wait_for_deploy(service_id, deploy_id):
                print()
                print("🎉 DEPLOYMENT COMPLETE!")
                print(f"🔗 Live URL: {service_url}")
                print()
        
    else:
        print("📦 No existing service found. Creating new service...")
        print()
        
        # Create new service
        service = create_service()
        
        if service and 'service' in service:
            svc = service['service']
            service_id = svc.get('id')
            service_name = svc.get('name')
            
            print(f"✅ Service created: {service_name}")
            print(f"   ID: {service_id}")
            print()
            
            # Set environment variables
            set_env_vars(service_id)
            print()
            
            # Get service URL
            time.sleep(2)
            service_url = get_service_url(service_id)
            
            if service_url:
                print(f"🎉 SERVICE CREATED SUCCESSFULLY!")
                print(f"🔗 URL: {service_url}")
                print()
                print("⏳ Note: First deployment may take 3-5 minutes")
                print(f"   Monitor at: https://dashboard.render.com")
                print()
            else:
                print("⚠️  Service created but URL not available yet")
                print("   Check Render dashboard for deployment status")
        else:
            print("❌ Failed to create service")
            sys.exit(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⏸️  Deployment interrupted")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)
