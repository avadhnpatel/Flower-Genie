$(document).ready(function () {
    // example: https://getbootstrap.com/docs/4.2/components/modal/
    // show modal
    $('#task-modal').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget) // Button that triggered the modal
        const userID = button.data('source') // Extract info from data-* attributes
        const name = button.data('name') // Extract info from data-* attributes
        const email = button.data('email')
        const password = button.data('password')

        const modal = $(this)
        if (userID === 'New Task') {
            modal.find('.modal-title').text(userID)
            $('#task-form-display').removeAttr('userID')
        } else {
            modal.find('.modal-title').text('Edit User ' + userID)
            $('#task-form-display').attr('taskID', userID)
        }

        if (name) {
            modal.find('.form-control0').val(name);
        } else {
            modal.find('.form-control0').val('');
        }

        if (email) {
            modal.find('.form-control1').val(email);
        } else {
            modal.find('.form-control1').val('');
        }

        if (password) {
            modal.find('.form-control2').val(password);
        } else {
            modal.find('.form-control2').val('');
        }
    })


    $('#submit-task').click(function () {
        const tID = $('#task-form-display').attr('taskID');
        console.log(document.getElementById('username').value, document.getElementById('email').value, document.getElementById('password').value)
        $.ajax({
            type: 'POST',
            url: tID ? '/edit/' + tID : '/create',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'username': document.getElementById('username').value,
                'email': document.getElementById('email').value,
                'password': document.getElementById('password').value
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('#search').click(function () {
        $.ajax({
            type: 'POST',
            url: '/', 
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'search': document.getElementById('search_request').value
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('.remove').click(function () {
        const remove = $(this)
        $.ajax({
            type: 'POST',
            url: '/delete/' + remove.data('source'),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('.state').click(function () {
        const state = $(this)
        const tID = state.data('source')
        const new_state = 0;
        if (state.text() === "In Progress") {
            new_state = "Complete"
        } else if (state.text() === "Complete") {
            new_state = "Todo"
        } else if (state.text() === "Todo") {
            new_state = "In Progress"
        }

        $.ajax({
            type: 'POST',
            url: '/edit/' + tID,
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'status': new_state
            }),
            success: function (res) {
                console.log(res)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

});