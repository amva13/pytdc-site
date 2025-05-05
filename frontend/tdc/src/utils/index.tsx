const handelTitle = (title: string): void => {
  if (typeof document !== 'undefined') {
    document.title = title;
  }
};

function Addshrink(): void {
  if (typeof window !== 'undefined' && typeof document !== 'undefined') {
    const RelBanner = document.querySelector('.classy-nav-container');
    if (RelBanner) {
      window.addEventListener('scroll', () => {
        if (window.pageYOffset > 86) {
          RelBanner.classList.add('sticky');
        } else {
          RelBanner.classList.remove('sticky');
        }
      });
    }
  }
}

const addActiveClass = (): void => {
  if (typeof document !== 'undefined') {
    const NavToggler = document.querySelector('.navbarToggler');
    if (NavToggler) {
      if (NavToggler.classList.contains('active')) {
        NavToggler.classList.remove('active');
      } else {
        NavToggler.classList.add('active');
      }
      OpenMenu();
    }
  }
};

const OpenMenu = (): void => {
  if (typeof document !== 'undefined') {
    const NavToggler = document.querySelector('.navbarToggler');
    const ClassyMenu = document.querySelector('.classy-menu');
    if (NavToggler && ClassyMenu) {
      if (NavToggler.classList.contains('active')) {
        ClassyMenu.classList.add('menu-on');
      } else {
        ClassyMenu.classList.remove('menu-on');
      }
    }
  }
};

const moveSmooth = (): void => {
  if (typeof window !== 'undefined') {
    window.scrollTo({
      behavior: 'smooth',
    });
  }
};

function loader(): void {
  if (typeof window !== 'undefined' && typeof document !== 'undefined') {
    const fadeTarget = document.getElementById('preloader');
    if (fadeTarget) {
      function fadeOutEffect() {
        const fadeEffect: NodeJS.Timeout = setInterval(() => {
          if (fadeTarget && fadeTarget.style.opacity && parseFloat(fadeTarget.style.opacity) > 0) {
            fadeTarget.style.opacity = (parseFloat(fadeTarget.style.opacity) - 0.1).toString();
          } else {
            clearInterval(fadeEffect);
            if (fadeTarget){
              fadeTarget.style.display = 'none';
            }
          }
        }, 100);
      }
      window.onload = (): ReturnType<typeof setTimeout> => setTimeout(fadeOutEffect, 1000); 
    }
  }
}

export {
  handelTitle,
  Addshrink,
  addActiveClass,
  OpenMenu,
  moveSmooth,
  loader,
};
