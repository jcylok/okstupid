// $(document).on("mouseover", function(){
    // if
    // $(document).scrollTop() > 86){
        // $("#banner").addClass("shrink");
    // }
    // else
    // {
    //     $("#banner").removeClass("shrink");
    // }
// });

$(document).on({
    mouseenter: function () {
        $("#banner").addClass("shrink");
    },
    mouseleave: function () {
        $("#banner").removeClass("shrink");
    }
});