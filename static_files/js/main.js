// Main

    // For nav bar  
    document.addEventListener('DOMContentLoaded', function() {
        var elems = document.querySelectorAll('.sidenav');
        var elems_right = document.querySelectorAll('.sidenav-right');
        var instances = M.Sidenav.init(elems);
        var instances = M.Sidenav.init(elems_right, {edge:'right'});
      });
    

    // For Popup    
    document.addEventListener('DOMContentLoaded', function() {
        var elems = document.querySelectorAll('.modal');
        var instances = M.Modal.init(elems);
    });


    // For Parallax
    $(document).ready(function () { 
        $('.parallax').parallax();
    });
