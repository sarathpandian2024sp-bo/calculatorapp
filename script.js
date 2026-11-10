const display = document.getElementById('display');

function appendValue(value) {
    if (display.value === 'Error') {
        display.value = '';
    }
    display.value += value;
}

function clearDisplay() {
    display.value = '';
}

function deleteLast() {
    if (display.value === 'Error') {
        display.value = '';
    } else {
        display.value = display.value.slice(0, -1);
    }
}

function calculate() {
    try {
        if (display.value.trim() !== '') {
            // Safely parse mathematical logic
            display.value = Function('"use strict";return (' + display.value + ')')();
        }
    } catch (error) {
        display.value = 'Error';
    }
}
