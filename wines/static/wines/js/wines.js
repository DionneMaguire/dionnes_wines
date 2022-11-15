    $('.btt-link').click(function (e) {
        window.scrollTo(0, 0)
    })

    $('#sort-selector').change(function () {
        var selector = $(this);
        var currentUrl = new URL(window.location);

        var selectedVal = selector.val();
        if (selectedVal != "reset") {
            var sort = selectedVal.split("_")[0];
            var direction = selectedVal.split("_")[1];

            currentUrl.searchParams.set("sort", sort);
            currentUrl.searchParams.set("direction", direction);

            window.location.replace(currentUrl);
        } else {
            currentUrl.searchParams.delete("sort");
            currentUrl.searchParams.delete("direction");

            window.location.replace(currentUrl);
        }
    })
    // confirmation before delete
    $('.delete_button').click(function(e){
        var result = confirm("Are you sure you want to delete this wine?");
        if(!result) {
            e.preventDefault();
        }
    });