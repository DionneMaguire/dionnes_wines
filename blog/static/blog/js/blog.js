    // handles back to top button
    $('.btt-link').click(function (e) {
        window.scrollTo(0, 0);
    });
    // confirmation before delete
    $('.delete_button').click(function(e){
        var result = confirm("Are you sure you want to delete this blog?");
        if(!result) {
            e.preventDefault();
        }
    });