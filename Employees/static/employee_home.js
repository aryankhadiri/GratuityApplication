/*
    var employees_info = {};
    {% for instance in list %}
        var name = "{{instance.name}}";
        var point = {{instance.point}};
        employees_info[name]=point
    {% endfor %}
    var x = document.getElementById("id_employee");
    
    */
   function addElement(){
    var totalForms = document.getElementById("id_form-TOTAL_FORMS").value;
    //forms ids start from 0
    var existing_row_employee = document.getElementById("id_form-0-employee");
    var new_row_employee = existing_row_employee.cloneNode(true);
    new_row_employee.id = "id_form-" + totalForms + "-employee";
    new_row_employee.name = "form-" + totalForms + "-employee";
    document.getElementById("names").appendChild(new_row_employee);
    
    var existing_row_point = document.getElementById("id_form-0-point");
    var new_row_point = existing_row_point.cloneNode(true);
    new_row_point.id = "id_form-" + totalForms + "-point";
    new_row_point.name = "form-" + totalForms + "-point";
    new_row_point.value = null;

    document.getElementById("indexes").appendChild(new_row_point);
    
    var existing_row_tip = document.getElementById("id_form-0-tip_amount");
    var new_row_tip = existing_row_tip.cloneNode(true);
    new_row_tip.id = "id_form-" + totalForms + "-tip_amount";
    new_row_tip.name = "form-" + totalForms + "-tip_amount";
    new_row_tip.value = null;
    document.getElementById("tips").appendChild(new_row_tip);

    var existing_row_paid_today = document.getElementById("id_form-0-paid_today");
    var new_row_paid_today = existing_row_paid_today.cloneNode(true);
    new_row_paid_today.id = "id_form-" + totalForms + "-paid_today";
    new_row_paid_today.name = "form-" + totalForms + "-paid_today";
    new_row_paid_today.value = null;
    document.getElementById("paid-todays").appendChild(new_row_paid_today);

    var existing_row_paid_later = document.getElementById("id_form-0-paid_later");
    var new_row_paid_later = existing_row_paid_later.cloneNode(true);
    new_row_paid_later.id = "id_form-" + totalForms + "-paid_later";
    new_row_paid_later.name = "form-" + totalForms + "-paid_later";
    new_row_paid_later.value = null;

    document.getElementById("paid-laters").appendChild(new_row_paid_later);

    totalForms = parseInt(totalForms) + 1;
    document.getElementById("id_form-TOTAL_FORMS").value = totalForms.toString();
   }
    
    /*
    for (i = 0; i<10; i++){
    var y = x.cloneNode(true)
    y.id = "id_employee"+i;

    var z = document.getElementById("names");

    z.appendChild(y);
   
}
}
var counter = 9;

function add_new_employee(){
    
}*/
 function total_cc_tip(doc){
     var cc_tip = parseInt(document.getElementById("cc_tip").value);
     var cc_t_tip = parseInt(doc.value) + cc_tip;
     document.getElementById("Total_Tip_By_Cards").value = cc_t_tip;
     document.getElementById("Total_Tip_By_Cards_2").value = cc_t_tip;
 }
function total_cash_sales(doc){
    var cash_sales = parseInt(document.getElementById("cash_sales").value);
    var total_cash = parseInt(doc.value) + cash_sales;
     document.getElementById("Total_Cash").value = total_cash;
     document.getElementById("cash_tip_2").value = parseInt(doc.value);
}
function total_tip(){
   var cc_tips = document.getElementById("Total_Tip_By_Cards_2").value;
   var cash_tip = document.getElementById("cash_tip_2").value;
   document.getElementById("Total_Tip").value = parseInt(cc_tips)+parseInt(cash_tip)
   document.getElementById("Total_Tip_2").value = parseInt(cc_tips)+parseInt(cash_tip)

}
function shift_tip_func(doc){
    var total_tip = document.getElementById("Total_Tip_2").value;
    var shift_tip = parseInt(total_tip)-parseInt(doc.value);
    document.getElementById("shift_tip").value = shift_tip;

}