/**
 * This script allows for the active dashboard link to be "highlighted."
 */
$(function() {
    switch(page) {
        case "Home": $("#nav ul li#list_item1 a").addClass("active");
            break;
        case "Add Employee": $("#nav ul li#list_item2 a").addClass("active");
            break;
        case "Edit Employee": $("#nav ul li#list_item3 a").addClass("active");
            break;
        case "New Form": $("#nav ul li#list_item1 a").addClass("active");
            break;
    }
});