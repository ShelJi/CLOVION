function hello() {
    // event.preventDefault();

    var name = document.getElementById('name').value;
    var number1 = document.getElementById('number1').value;
    var email = document.getElementById('exampleInputEmail1').value;
    var password = document.getElementById('exampleInputPassword1').value;

    show(name, number1, email, password);
}

function show(name, number1, email, password) {
    document.getElementById('display_name').innerHTML = name;
    document.getElementById('display_number').innerHTML = number(number1);
    document.getElementById('display_email').innerHTML = email;
    document.getElementById('display_password').innerHTML = password;
}

function number(number1) {
    let number="";
    if (number1 % 2 == 0) {
        return number = "even";
    }
    else {
        return number = "odd";
    }
}
