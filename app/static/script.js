document.addEventListener('DOMContentLoaded', function() {
    const predictionForm = document.getElementById('predictionForm');
    const resultCard = document.getElementById('resultCard');
    const predictedPrice = document.getElementById('predictedPrice');
    
    // View slider value display
    const viewSlider = document.getElementById('view');
    const viewValue = document.getElementById('viewValue');
    
    viewSlider.addEventListener('input', function() {
        viewValue.textContent = this.value;
    });
    
    // Condition slider value display
    const conditionSlider = document.getElementById('condition');
    const conditionValue = document.getElementById('conditionValue');
    
    conditionSlider.addEventListener('input', function() {
        conditionValue.textContent = this.value;
    });
    
    // Set current year as default for year fields
    const currentYear = new Date().getFullYear();
    document.getElementById('year_built').max = currentYear;
    document.getElementById('year_renovated').max = currentYear;
    
    // Form submission
    predictionForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Year validation
        const yearBuilt = parseInt(document.getElementById('year_built').value);
        const yearRenovated = document.getElementById('year_renovated').value;
        
        if (yearRenovated && parseInt(yearRenovated) < yearBuilt) {
            alert('Year renovated cannot be earlier than year built');
            return;
        }
        
        // Create FormData object
        const formData = new FormData(predictionForm);
        
        // Add checkbox value correctly
        formData.set('waterfront', document.getElementById('waterfront').checked);
        
        // Submit form data
        fetch('/predict/', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                return response.json().then(err => { throw new Error(err.detail || 'Error making prediction') });
            }
            return response.json();
        })
        .then(data => {
            // Format the price with commas and currency
            const formattedPrice = new Intl.NumberFormat('en-US', {
                style: 'currency',
                currency: data.currency || 'USD',
                maximumFractionDigits: 0
            }).format(data.prediction);
            
            // Show result
            predictedPrice.textContent = formattedPrice;
            resultCard.classList.remove('d-none');
            resultCard.classList.add('show');
            
            // Smooth scroll to result
            resultCard.scrollIntoView({ behavior: 'smooth', block: 'center' });
        })
        .catch(error => {
            alert(error.message);
            console.error('Error:', error);
        });
    });
});
