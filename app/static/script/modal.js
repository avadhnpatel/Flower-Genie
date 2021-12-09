$(document).ready(function () {
    // example: https://getbootstrap.com/docs/4.2/components/modal/
    // show modal
    $('#task-modal-user').on('show.bs.modal', function (event) {
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



    $('#submit-user').click(function () {
        const tID = $('#task-form-display').attr('taskID');
        console.log(document.getElementById('username').value, document.getElementById('email').value, document.getElementById('password').value)
        $.ajax({
            type: 'POST',
            url: tID ? '/user/edit/' + tID : '/user/create',
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

    $('#myButton').click(function () {
        console.log("hello");
    });


    $('#search-user').click(function () {
        $.ajax({
            type: 'POST',
            url: '/user',
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
            url: '/user/delete/' + remove.data('source'),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('#task-modal-wishlist').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget) // Button that triggered the modal
        const wishlistID = button.data('source') // Extract info from data-* attributes
        const userID = button.data('userID') // Extract info from data-* attributes
        const occasion = button.data('occasion')
        const arrangementID = button.data('arrangementID')

        const modal = $(this)
        if (wishlistID === 'New Task') {
            modal.find('.modal-title').text(wishlistID)
            $('#task-form-display-w').removeAttr('wishlistID')
        } else {
            modal.find('.modal-title').text('Edit Wishlist ' + wishlistID)
            $('#task-form-display-w').attr('taskID', wishlistID)
        }

        if (userID) {
            modal.find('.form-control0').val(userID);
        } else {
            modal.find('.form-control0').val('');
        }

        if (occasion) {
            modal.find('.form-control1').val(occasion);
        } else {
            modal.find('.form-control1').val('');
        }

        if (arrangementID) {
            modal.find('.form-control2').val(arrangementID);
        } else {
            modal.find('.form-control2').val('');
        }
    });

    $('#task-modal-answer').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget) // Button that triggered the modal
        const answersID = button.data('answersID') // Extract info from data-* attributes
        const userID = button.data('userID') // Extract info from data-* attributes
        const arrangementID = button.data('arrangementID')
        const party_Size = button.data('party_Size')
        const budget = button.data('budget')
        const preferred_Flower = button.data('preferred_Flower')
        const preferred_Color = button.data('preferred_Color')
        const preferred_Style = button.data('preferred_Style')
        const satisfaction = button.data('satisfaction')

        const modal = $(this)
        if (wishlistID === 'New Task') {
            modal.find('.modal-title').text(wishlistID)
            $('#task-form-display-w').removeAttr('wishlistID')
        } else {
            modal.find('.modal-title').text('Edit Wishlist ' + wishlistID)
            $('#task-form-display-w').attr('taskID', wishlistID)
        }

        if (answersID) {
            modal.find('.form-control0').val(answersID);
        } else {
            modal.find('.form-control0').val('');
        }

        if (userID) {
            modal.find('.form-control1').val(userID);
        } else {
            modal.find('.form-control1').val('');
        }

        if (arrangementID) {
            modal.find('.form-control2').val(arrangementID);
        } else {
            modal.find('.form-control2').val('');
        }

        if (party_Size) {
            modal.find('.form-control2').val(party_Size);
        } else {
            modal.find('.form-control2').val('');
        }

        if (budget) {
            modal.find('.form-control2').val(budget);
        } else {
            modal.find('.form-control2').val('');
        }

        if (preferred_Flower) {
            modal.find('.form-control2').val(preferred_Flower);
        } else {
            modal.find('.form-control2').val('');
        }

        if (preferred_Color) {
            modal.find('.form-control2').val(preferred_Color);
        } else {
            modal.find('.form-control2').val('');
        }

        if (preferred_Style) {
            modal.find('.form-control2').val(preferred_Style);
        } else {
            modal.find('.form-control2').val('');
        }

        if (satisfaction) {
            modal.find('.form-control2').val(satisfaction);
        } else {
            modal.find('.form-control2').val('');
        }
    });

    $('#task-modal-q1').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget) // Button that triggered the modal
        // const wishlistID = button.data('source') // Extract info from data-* attributes
        const name = button.data('name') // Extract info from data-* attributes
        const budget = button.data('budget')

        const modal = $(this)
        // if (wishlistID === 'New Task') {
        //     modal.find('.modal-title').text(wishlistID)
        //     $('#task-form-display-q1').removeAttr('wishlistID')
        // } else {
        //     modal.find('.modal-title').text('Edit Wishlist ' + wishlistID)
        //     $('#task-form-display-q1').attr('taskID', wishlistID)
        // }

        if (name) {
            modal.find('.form-control0').val(name);
        } else {
            modal.find('.form-control0').val('');
        }

        if (budget) {
            modal.find('.form-control1').val(budget);
        } else {
            modal.find('.form-control1').val('');
        }


    });

    $('#search-wishlist').click(function () {
        $.ajax({
            type: 'POST',
            url: '/wishlist',
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

    $('#submit-wishlist').click(function () {
        const tID = $('#task-form-display-w').attr('taskID');
        console.log(document.getElementById('arrangementID').value, document.getElementById('userID').value, document.getElementById('occasion').value)
        console.log(document.getElementById('userID').value);
        console.log(tID);
        $.ajax({
            type: 'POST',
            url: tID ? '/wishlist/edit/' + tID : '/wishlist/create',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'userID': document.getElementById('userID').value,
                'occasion': document.getElementById('occasion').value,
                'arrangementID': document.getElementById('arrangementID').value
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


    $('.removeWishlist').click(function () {
        const remove = $(this)
        $.ajax({
            type: 'POST',
            url: '/wishlist/delete/' + remove.data('source'),
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
