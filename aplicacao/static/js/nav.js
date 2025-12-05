document.addEventListener('DOMContentLoaded', function() {
    const tituloMenu = document.querySelectorAll('nav>ul>li>a');

    tituloMenu.forEach(header => {
        header.addEventListener('click', function() {
            const menuItem = this.parentElement;

            const submenu = menuItem.querySelector('nav>ul>li>ul');

            const menuPrincipal = menuItem.parentElement;
            
            // Fecha outros submenus
            closeOtherSubmenus(menuItem);
            
            // Alterna o submenu atual
            menuItem.classList.toggle('ativo');
            submenu.classList.toggle('ativo');
        });
    });
});

function closeOtherSubmenus(currentMenuItem) {
    const allMenuItems = document.querySelectorAll('nav>ul>li');
    
    allMenuItems.forEach(item => {
        if (item !== currentMenuItem) {
            const submenu = item.querySelector('nav>ul>li>ul');
            
            item.classList.remove('ativo');
            submenu.classList.remove('ativo');
        }
    });
}