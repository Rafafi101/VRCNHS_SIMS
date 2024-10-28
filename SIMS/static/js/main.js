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
            });
        });
    });
});

// Add jQuery and DataTables scripts to main.js
$.getScript("https://code.jquery.com/jquery-3.6.4.min.js", function() {
    $.getScript("https://cdn.datatables.net/1.11.5/js/jquery.dataTables.min.js", function() {
        $(document).ready(function () {
            $('#teachersTable').DataTable({
            });
        });
    });
});

$.getScript("https://code.jquery.com/jquery-3.6.4.min.js", function() {
    $.getScript("https://cdn.datatables.net/1.11.5/js/jquery.dataTables.min.js", function() {
        $(document).ready(function () {
            $('#classroom-table-7').DataTable({});
            $('#classroom-table-8').DataTable({});
            $('#classroom-table-9').DataTable({});
            $('#classroom-table-10').DataTable({});
            $('#classroom-table-11').DataTable({});
            $('#classroom-table-12').DataTable({});
            $('#student-table-grade8').DataTable({});
            $('#student-table-grade9').DataTable({});
            $('#student-table-grade10').DataTable({});
            $('#student-table-grade11').DataTable({});
            $('#student-table-grade12').DataTable({});
            $('#for-departure').DataTable({});

        });
    });
});


//<!-- DataTables Initialization -->
$(document).ready(function () {
    
});

$(document).ready(function() {
$('#datepicker').datepicker({
    format: 'yyyy-mm-dd',
    autoclose: true,
    todayHighlight: true
});
});

document.getElementById("confirmBulkPromoteButton").addEventListener("click", function () {
    $.ajax({
        url: "{% url 'bulk_promote_students' %}",
        method: "POST",
        headers: {
            "X-CSRFToken": "{{ csrf_token }}"
        },
        success: function(response) {
            if (response.success) {
                // Reload the page to reflect changes
                location.reload();
            } else {
                alert(response.message);
            }
        },
        error: function(xhr, status, error) {
            alert("An error occurred while promoting students.");
        }
    });
});

