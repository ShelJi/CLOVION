// first part
function values() {
    var data = document.getElementById('data').value;
    display(data);
}

function display(data) {
    // display data
    document.getElementById('value').innerHTML = data;
    // prime number
    if (!isNaN(data)) {
        if (data !== "0") {

            if (Prime(data)) {
                document.getElementById('prime').innerHTML = data + " is not a prime number";
            }
            else {
                document.getElementById('prime').innerHTML = data + " is a prime number";
            }
            // amstrong number
            if (amstrong(data)) {
                document.getElementById('amstrong').innerHTML = data + " amstrong number";
            }
            else {
                document.getElementById('amstrong').innerHTML = data + " not amstrong number";
            }
        }
        else {
            document.getElementById('prime').innerHTML = "0 is neither prime nor composite.";
            document.getElementById('amstrong').innerHTML = "0 is an amstrong number";
        }
    }
    // reverse numbers
    reverse_number(data);
}

function Prime(data) {

    if (data !== "1") {
        for (let i = 2; i < data; i++) {
            if (data % i === 0) {
                return true;
            }
        }
        return false;
    }
    else {
        return true;
    }
}

function reverse_number(data) {
    const reversed = data.split('').reverse().join('');
    document.getElementById('reversed').innerHTML = reversed + " reversed of input";
}

function amstrong(data) {
    var ams = 0;
    for (let i = 1; i < data; i++) {
        if (i % 2 === 0) {
            ams += i;
        }
    }
    num_data = Number(data);
    console.log(ams);
    if (ams === num_data) {
        return true;
    }
    else {
        return false;
    }
}
// ********************************

// operators
function opp_values() {
    var opp1_val = document.getElementById('operator1').value;
    var opp2_val = document.getElementById('operator2').value;

    const opp1 = Number(opp1_val);
    const opp2 = Number(opp2_val);

    addition(opp1, opp2);
    subtraction(opp1, opp2);
    multiplication(opp1, opp2);
    division(opp1, opp2);
}

function addition(opp1, opp2) {
    let ans = opp1 + opp2;
    document.getElementById('addition').innerHTML = "addition is " + ans;
}
function subtraction(opp1, opp2) {
    let ans = opp1 - opp2;
    document.getElementById('subtraction').innerHTML = "subtraction is " + ans;
}
function multiplication(opp1, opp2) {
    let ans = opp1 * opp2;
    document.getElementById('multiplication').innerHTML = "multiplication is " + ans;
}
function division(opp1, opp2) {
    let ans = opp1 / opp2;
    document.getElementById('division').innerHTML = "division is " + ans;
}
// ********************************
