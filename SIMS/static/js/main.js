const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(function() {
    $('#message').fadeOut('slow');
}, 10000);

// Add jQuery and DataTables scripts to main.js
$.getScript("https://code.jquery.com/jquery-3.6.4.min.js", function() {
    $.getScript("https://cdn.datatables.net/1.11.5/js/jquery.dataTables.min.js", function() {
        $(document).ready(function () {
            $('#studentTable').DataTable({
                paging: true, // Enable pagination
                searching: true, // Enable searching
                ordering: true, // Enable column ordering
                info: true // Show table information
            });
        });
    });
});

// Add jQuery and DataTables scripts to main.js
$.getScript("https://code.jquery.com/jquery-3.6.4.min.js", function() {
    $.getScript("https://cdn.datatables.net/1.11.5/js/jquery.dataTables.min.js", function() {
        $(document).ready(function () {
            $('#teachersTable').DataTable({
                paging: true, // Enable pagination
                searching: true, // Enable searching
                ordering: true, // Enable column ordering
                info: true // Show table information
            });
        });
    });
});

$(document).ready(function() {
$('#datepicker').datepicker({
    format: 'yyyy-mm-dd',
    autoclose: true,
    todayHighlight: true
});
});

