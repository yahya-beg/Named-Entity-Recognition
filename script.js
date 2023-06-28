function analyzeText() {
    var text = document.getElementById('textInput').value;

    // Send the text to the backend for analysis
    fetch('http://127.0.0.1:5000/analyze', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: text })
    })
    .then(response => response.json())
    .then(data => {
        displayResult(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}



function displayResult(result) {
    var resultDiv = document.getElementById('result-container');
    resultDiv.innerHTML = '<div class="result-box"></div>';

    if (result.error) {
        resultDiv.innerHTML = '<p class="error-message">An error occurred: ' + result.error + '</p>';
    } else {
        if (result.entities.length === 0) {
            resultDiv.innerHTML = '<p>No named entities found.</p>';
        } else {
            for (var i = 0; i < result.entities.length; i++) {
                var entity = result.entities[i];
                var entityText = document.createElement('p');
                entityText.textContent = 'Text: ' + entity.text + '  ------------->    Label: ' + entity.label;
                resultDiv.appendChild(entityText);
            }
        }
    }
}
