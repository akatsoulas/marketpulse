$(document).ready(function() {
    'use strict';

    $('#planprices-addfield').click(function() {
        $(".planprices:first").clone().appendTo("#fieldset-planprices");
        return false;
    });

    function displayLocationForm () {
        var choice = $("#id_is_online:checked").val();

        if (choice === 'on') {
            $("#location").hide();
            $("#onlineshop").show();
        } else {
            $("#location").show();
            $("#onlineshop").hide();
        }
    }

    $(document).on("click", ".hasplan-check", function () {
        var n = $(this.checked).length;

        if (n === 0) {
            $(this).closest(".planprices").find('.hasplan').hide();
        } else {
            $(this).closest(".planprices").find('.hasplan').show();
        }
    });

    $('#id_is_online').on('change', displayLocationForm);
    displayLocationForm();
});
