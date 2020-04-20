
    
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


var dictionaryFromServer = document.getElementById("query").value
var dictionary = JSON.parse(dictionaryFromServer);
console.log(dictionary)
/*
dictionary = {'employee_id':'point'}
*/
/*
function getIndexOfEmployee(doc){
   var selectedEmployeeId = doc.value
   var index = dictionary[selectedEmployeeId];
   var name_input_id = doc.id;
   console.log(name_input_id)
   arr = name_input_id.split("-");
   console.log(arr);
   performance_index_id_constructor = arr[0]+"-"+arr[1]+"-point";
   console.log(performance_index_id_constructor)
   document.getElementById(performance_index_id_constructor).value = index
}
*/
function getIndexOfEmployee(doc){
    var selectedEmployeeId = doc.value
    index = relativeIndexFinder(doc)
    document.getElementById("indexes").children[index].value = dictionary[selectedEmployeeId]
}
function relativeIndexFinder(doc){
    //finds out which element of the div is changing, returns the index of the element in the children array
    var parentElement = doc.parentNode;
    var index = Array.prototype.indexOf.call(parentElement.children, doc);
    return index
}
function paidLaterCalculator(doc){
    index = relativeIndexFinder(doc);
    var total_tip = parseInt(document.getElementById("tips").children[index].value);
    var paid_today = parseInt(doc.value)
    var paid_later = total_tip-paid_today;
    document.getElementById("paid-laters").children[index].value = paid_later
}
function calculateTotalIndex(doc){
    var sum = 0;
    var indexes = document.getElementById("indexes");
    for (i = 1; i < indexes.children.length; i++){
        sum += parseFloat(indexes.children[i].value);
    }
    doc.value = sum;
}
