// Intersection Observer for Scroll Animations
document.addEventListener('DOMContentLoaded', () => {
    
    // Select all elements with the 'reveal' class
    const reveals = document.querySelectorAll('.reveal');

    // Options for the Intersection Observer
    const revealOptions = {
        threshold: 0.15, // Trigger when 15% of the element is visible
        rootMargin: "0px 0px -50px 0px"
    };

    // Callback function for the observer
    const revealOnScroll = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                // Optional: Stop observing once revealed
                observer.unobserve(entry.target);
            }
        });
    }, revealOptions);

    // Start observing each element
    reveals.forEach(reveal => {
        revealOnScroll.observe(reveal);
    });

    // Smooth scroll for anchor links (safeguard for cross-browser support)
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Ensure hero section is revealed on load immediately
    setTimeout(() => {
        const heroContent = document.querySelector('.hero-content.reveal');
        if (heroContent) {
            heroContent.classList.add('active');
        }
    }, 100);
});
