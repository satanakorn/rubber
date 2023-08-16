function calculateBMI() {
    const weight = parseFloat(document.getElementById("weight").value);
    const height = parseFloat(document.getElementById("height").value) / 100;
  
    if (isNaN(weight) || isNaN(height)) {
      alert("Please enter valid weight and height.");
      return;
    }
  
    const bmi = weight / (height * height);
    const bmiMessage = getBMIMessage(bmi);
  
    document.getElementById("result").innerHTML = `Your BMI is ${bmi.toFixed(1)}. ${bmiMessage}`;
  }
  
  function getBMIMessage(bmi) {
    if (bmi < 18.5) {
      return "You are underweight.";
    } else if (bmi >= 18.5 && bmi <= 24.9) {
      return "You have a healthy weight.";
    } else if (bmi >= 25 && bmi <= 29.9) {
      return "You are overweight.";
    } else {
      return "You are obese.";
    }
  }
  