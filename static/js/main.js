/**
 * 5th Corner — Main JavaScript
 * Handles scroll animations, navigation, and section transitions
 */

(function() {
    'use strict';

    /* ========================================
       NAVIGATION
       ======================================== */

    function initNavigation() {
        const nav = document.getElementById('siteNav');
        const toggle = document.getElementById('navToggle');
        const mobileMenu = document.getElementById('mobileMenu');

        if (!nav) return;

        // Scroll-based nav background
        let lastScroll = 0;
        window.addEventListener('scroll', function() {
            const currentScroll = window.pageYOffset;
            if (currentScroll > 50) {
                nav.classList.add('scrolled');
            } else {
                nav.classList.remove('scrolled');
            }
            lastScroll = currentScroll;
        }, { passive: true });

        // Mobile menu toggle
        if (toggle && mobileMenu) {
            toggle.addEventListener('click', function() {
                toggle.classList.toggle('active');
                mobileMenu.classList.toggle('active');
                document.body.style.overflow = mobileMenu.classList.contains('active') ? 'hidden' : '';
            });

            // Close mobile menu on link click
            mobileMenu.querySelectorAll('.mobile-menu-link').forEach(function(link) {
                link.addEventListener('click', function() {
                    toggle.classList.remove('active');
                    mobileMenu.classList.remove('active');
                    document.body.style.overflow = '';
                });
            });
        }
    }

    /* ========================================
       SCROLL REVEAL ANIMATIONS
       ======================================== */

    function initScrollReveal() {
        var revealSelectors = [
            '.content-label',
            '.content-heading',
            '.content-body',
            '.project-links',
            '.studio-heading',
            '.studio-body',
            '.studio-cta'
        ];

        var observer = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.15,
            rootMargin: '0px 0px -80px 0px'
        });

        revealSelectors.forEach(function(selector) {
            document.querySelectorAll(selector).forEach(function(el) {
                observer.observe(el);
            });
        });
    }

    /* ========================================
       PARALLAX-LIKE BACKGROUND SCALING
       ======================================== */

    function initSectionObserver() {
        var sections = document.querySelectorAll('.section');

        var observer = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('in-view');
                } else {
                    entry.target.classList.remove('in-view');
                }
            });
        }, {
            threshold: 0.2
        });

        sections.forEach(function(section) {
            observer.observe(section);
        });
    }

    /* ========================================
       SMOOTH ANCHOR SCROLLING
       ======================================== */

    function initSmoothScroll() {
        document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
            anchor.addEventListener('click', function(e) {
                var href = this.getAttribute('href');
                if (href === '#') return;

                var target = document.querySelector(href);
                if (target) {
                    e.preventDefault();
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });
    }

    /* ========================================
       SCROLL INDICATOR HIDE ON SCROLL
       ======================================== */

    function initScrollIndicator() {
        var indicator = document.getElementById('scrollIndicator');
        if (!indicator) return;

        var hidden = false;
        window.addEventListener('scroll', function() {
            if (!hidden && window.pageYOffset > 100) {
                indicator.style.opacity = '0';
                indicator.style.transition = 'opacity 0.5s ease';
                hidden = true;
            }
        }, { passive: true });
    }

    /* ========================================
       BACKGROUND MEDIA SETUP
       ======================================== */

    function initBackgroundMedia() {
        var mediaSections = {
            'heroBg': '/static/images/hero.gif',
            'gamesBg': '/static/images/games-bg.gif',
            'filmBg': '/static/images/film-bg.gif',
            'vfxBg': '/static/images/vfx-bg.gif',
            'studioBg': '/static/images/studio-bg.gif'
        };

        Object.keys(mediaSections).forEach(function(id) {
            var el = document.getElementById(id);
            if (!el) return;

            var src = mediaSections[id];

            if (src.match(/\.(mp4|webm)$/i)) {
                var video = document.createElement('video');
                video.autoplay = true;
                video.loop = true;
                video.muted = true;
                video.playsInline = true;
                video.src = src;
                el.appendChild(video);
            } else {
                el.style.backgroundImage = 'url(' + src + ')';
            }
        });
    }

    /* ========================================
       PAGE SCROLL ANIMATIONS (for subpages)
       ======================================== */

    function initPageAnimations() {
        var animElements = document.querySelectorAll(
            '.feature-card, .media-item, .page-section'
        );

        if (animElements.length === 0) return;

        var observer = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                    observer.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        });

        animElements.forEach(function(el) {
            el.style.opacity = '0';
            el.style.transform = 'translateY(20px)';
            el.style.transition = 'opacity 0.6s ease, transform 0.6s cubic-bezier(0.16, 1, 0.3, 1)';
            observer.observe(el);
        });
    }

    /* ========================================
       INITIALIZE
       ======================================== */

    function init() {
        initNavigation();
        initScrollReveal();
        initSectionObserver();
        initSmoothScroll();
        initScrollIndicator();
        initBackgroundMedia();
        initPageAnimations();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

})();
