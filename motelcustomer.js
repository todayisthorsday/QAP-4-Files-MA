const MotelCustomer = {
  customerName: "Melanie Adams",
  dateOfBirth: "1989-11-15",
  gender: "F",
  roomPreferences: ["Balcony", " Ocean View"],
  paymentMethod: "Credit",
  mailingAddress: {
    street: "11 Adams Place",
    city: "Clarenville",
    province: "Newfoundland",
    postalCode: "A1A 1A1",
  },
  phoneNumber: "709-427-1234",
  checkIn: new Date("2024-07-24"),
  checkOut: new Date("2024-07-26"),
};

// Method to calculate the age of the customer
let getAge = (person) => {
  let thisYear = new Date().getFullYear();
  let birthYear = new Date(person).getFullYear();

  age = thisYear - birthYear;

  return age;
};

// Method to calculate the duration of stay in days
let stayDuration = () => {
  let checkInTime = MotelCustomer.checkIn.getTime();
  let checkOutTime = MotelCustomer.checkOut.getTime();

  durationTime = checkOutTime - checkInTime;

  durationDays = durationTime / (1000 * 60 * 60 * 24);

  return durationDays;
};

// Method to generate a description of the customer
const customerDescription = `
      <p>
    Name: ${MotelCustomer.customerName}<br> 
    Age: ${getAge(MotelCustomer.dateOfBirth)}<br> 
    Gender: ${MotelCustomer.gender}<br> 
    Room Preferences: ${MotelCustomer.roomPreferences}<br> 
    Payment Method: ${MotelCustomer.paymentMethod}<br> 
    Mailing Address:<br>
    ${MotelCustomer.mailingAddress.street}<br> 
    ${MotelCustomer.mailingAddress.city},<br>
    ${MotelCustomer.mailingAddress.province}<br> 
    ${MotelCustomer.mailingAddress.postalCode}<br> 
    Phone Number: ${MotelCustomer.phoneNumber} </p>
    <p>Check-in Date: ${MotelCustomer.checkIn.toDateString()}<br> 
    Check-out Date: ${MotelCustomer.checkOut.toDateString()}<br> 
    Duration of Stay: ${stayDuration()} days
    </p>
    `;

document.getElementById("customer-description").innerHTML = customerDescription;

console.log(stayDuration());
