# How to Get Your Discord Invite Link

## Step 1: Open Your Discord Server

1. Open Discord (desktop app or web)
2. Navigate to your R.A.S.T.E.R. game server

---

## Step 2: Create a Permanent Invite

### Method A: Right-click Channel (Easiest)

1. **Right-click** any text channel (like #general)
2. Click **"Invite People"**
3. Click **"Edit invite link"** at the bottom
4. Configure these settings:
   ```
   Expire after:         Never ← IMPORTANT!
   Max number of uses:   No limit
   Grant temporary membership: Off (recommended)
   ```
5. Click **"Generate a New Link"**
6. **Copy the invite link**

### Method B: Server Settings

1. Click your server name at the top
2. Click **"Invite People"**
3. Follow steps 3-6 above

---

## Step 3: Your Invite Link

You should now have a link that looks like:
```
https://discord.gg/nZCBjWsM
```

**The important part is the code at the end:** `nZCBjWsM`

---

## Step 4: Update Your Website

### Option 1: I Can Update It For You

Just paste your Discord invite link here and I'll update the `.env` file automatically.

### Option 2: Manual Update

1. Open the `.env` file in your project
2. Find this line:
   ```
   DISCORD_INVITE=https://discord.gg/YOUR_INVITE_CODE
   ```
3. Replace with your actual invite:
   ```
   DISCORD_INVITE=https://discord.gg/nZCBjWsM
   ```
4. Save the file
5. Restart Flask: `python app.py`

---

## Step 5: Test It

1. Go to http://localhost:5000
2. Click "JOIN DISCORD TO PLAY" button
3. Should open your Discord server

---

## Current Status

**Your .env file currently has:**
```
DISCORD_INVITE=https://discord.gg/nZCBjWsM
```

**Is this correct?** 
- If YES: You're all set!
- If NO: Get your real invite link and paste it here

---

## Troubleshooting

### "Invite expired or invalid"
- Make sure you set "Expire after" to **Never**
- Create a new invite with the steps above

### "Wrong server"
- Make sure you're creating the invite from your R.A.S.T.E.R. server
- Not a different Discord server

### "Don't have permission"
- You need "Create Invite" permission
- Ask the server owner to give you permission
- Or have them create the invite

---

## Important Notes

✅ **Make it permanent:** Set "Expire after" to **Never**  
✅ **Unlimited uses:** Set "Max uses" to **No limit**  
✅ **Test it:** Open the link in incognito to verify it works  
✅ **Keep it safe:** Anyone with this link can join your server  

---

**Ready to update?** Just paste your Discord invite link and I'll configure it!


