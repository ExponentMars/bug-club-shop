document.addEventListener('DOMContentLoaded', function() {
  const featured = document.getElementById('featured-section');
  if (featured) {
    featured.style.opacity = '0';
    featured.style.transition = 'opacity 1s ease-in-out';
  }

  window.addEventListener('scroll', function() {
    const banner = document.querySelector('.banner');
    if (banner && featured) {
      const bannerHeight = banner.offsetHeight;
      if (window.scrollY > bannerHeight * 0.5) {
        featured.style.opacity = '1';
      }
    }
  });
});