/**
 * R.A.S.T.E.R. - Main JavaScript
 * Minimal interactivity for landing page
 */

(function() {
    'use strict';
    
    /**
     * Smooth scroll for anchor links
     */
    function initSmoothScroll() {
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                const href = this.getAttribute('href');
                if (href === '#') return;
                
                e.preventDefault();
                const target = document.querySelector(href);
                
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });
    }
    
    /**
     * Track CTA button clicks (for analytics if needed)
     */
    function initCTATracking() {
        document.querySelectorAll('.cta-button').forEach(button => {
            button.addEventListener('click', function(e) {
                const buttonText = this.textContent.trim();
                console.log('CTA clicked:', buttonText);
                
                // Add analytics tracking here if needed
                // Example: gtag('event', 'cta_click', { button_text: buttonText });
            });
        });
    }
    
    /**
     * Add VHS static effect on hero section hover
     */
    function initVHSEffect() {
        const hero = document.querySelector('.hero');
        if (!hero) return;
        
        hero.addEventListener('mouseenter', function() {
            this.style.animation = 'vhs-static 0.3s';
        });
        
        hero.addEventListener('animationend', function() {
            this.style.animation = '';
        });
    }
    
    /**
     * Lazy load images for performance
     */
    function initLazyLoading() {
        if ('loading' in HTMLImageElement.prototype) {
            // Native lazy loading supported
            const images = document.querySelectorAll('img[loading="lazy"]');
            images.forEach(img => {
                img.src = img.src;
            });
        } else {
            // Fallback for browsers that don't support native lazy loading
            const script = document.createElement('script');
            script.src = 'https://cdnjs.cloudflare.com/ajax/libs/lazysizes/5.3.2/lazysizes.min.js';
            document.body.appendChild(script);
        }
    }
    
    /**
     * Add glitch effect to random text elements periodically
     */
    function initRandomGlitch() {
        const glitchElements = document.querySelectorAll('.hero-title, .section-title');
        
        function triggerGlitch() {
            const randomElement = glitchElements[Math.floor(Math.random() * glitchElements.length)];
            if (randomElement) {
                randomElement.style.animation = 'glitch-anim 0.3s';
                setTimeout(() => {
                    randomElement.style.animation = '';
                }, 300);
            }
        }
        
        // Trigger glitch every 10-15 seconds
        setInterval(triggerGlitch, 10000 + Math.random() * 5000);
    }
    
    /**
     * Detect scroll and add fade-in effects
     */
    function initScrollAnimations() {
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -100px 0px'
        };
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                    observer.unobserve(entry.target);
                }
            });
        }, observerOptions);
        
        // Observe elements that should fade in on scroll
        document.querySelectorAll('.feature-item, .gallery-item, .choice-card').forEach(el => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(20px)';
            el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
            observer.observe(el);
        });
    }
    
    /**
     * Handle image load errors (show placeholder)
     */
    function initImageErrorHandling() {
        document.querySelectorAll('.gallery-image').forEach(img => {
            img.addEventListener('error', function() {
                // Create placeholder if image fails to load
                this.src = 'data:image/svg+xml,%3Csvg xmlns="http://www.w3.org/2000/svg" width="400" height="300"%3E%3Crect width="400" height="300" fill="%231A1A1A"/%3E%3Ctext x="50%25" y="50%25" dominant-baseline="middle" text-anchor="middle" font-family="monospace" font-size="14" fill="%23E0E0E0"%3E[TAPE CORRUPTED]%3C/text%3E%3C/svg%3E';
                this.alt = 'Image not available';
            });
        });
    }
    
    /**
     * Handle choice card modal
     */
    function initChoiceModal() {
        const modal = document.getElementById('choiceModal');
        const modalTitle = document.getElementById('modalTitle');
        const modalDescription = document.getElementById('modalDescription');
        const modalClose = document.querySelector('.modal-close');
        const modalOverlay = document.querySelector('.modal-overlay');
        
        if (!modal) return;
        
        // Open modal when choice card is clicked
        document.querySelectorAll('.choice-card.clickable').forEach(card => {
            card.addEventListener('click', function(e) {
                const title = this.getAttribute('data-choice-title');
                const description = this.getAttribute('data-choice-description');
                
                modalTitle.textContent = title;
                modalDescription.textContent = description;
                modal.classList.add('active');
                document.body.style.overflow = 'hidden';
            });
        });
        
        // Close modal function
        function closeModal() {
            modal.classList.remove('active');
            document.body.style.overflow = '';
        }
        
        // Close on X button
        if (modalClose) {
            modalClose.addEventListener('click', closeModal);
        }
        
        // Close on overlay click
        if (modalOverlay) {
            modalOverlay.addEventListener('click', closeModal);
        }
        
        // Close on Escape key
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape' && modal.classList.contains('active')) {
                closeModal();
            }
        });
    }
    
    /**
     * Initialize all functions when DOM is ready
     */
    function init() {
        initSmoothScroll();
        initCTATracking();
        initVHSEffect();
        initLazyLoading();
        initRandomGlitch();
        initScrollAnimations();
        initImageErrorHandling();
        initChoiceModal();
        
        console.log('R.A.S.T.E.R. initialized');
    }
    
    // Run init when DOM is fully loaded
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
    
})();

