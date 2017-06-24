// // var paypal = require('paypal-rest-sdk');
// // $('#submit').click({
// //
// // paypal.configure({
// //   'mode': 'sandbox', //sandbox or live
// //   'client_id': 'EBWKjlELKMYqRNQ6sYvFo64FtaRLRR5BdHEESmha49TM',
// //   'client_secret': 'EO422dn3gQLgDbuwqTjzrFgFtaRLRR5BdHEESmha49TM'
// // });var card_data = {
// //   "type": "visa",
// //   "number": "4417119669820331",
// //   "expire_month": "11",
// //   "expire_year": "2018",
// //   "cvv2": "123",
// //   "first_name": "Joe",
// //   "last_name": "Shopper"
// // };
// //
// // paypal.creditCard.create(card_data, function(error, credit_card){
// //   if (error) {
// //     console.log(error);
// //     throw error;
// //   } else {
// //     console.log("Create Credit-Card Response");
// //     console.log(credit_card);
// //   }
// // })
// // // )};
// // paypal.Button.render({
// //
// //           env: 'production', // Or 'sandbox',
// //
// //           commit: true, // Show a 'Pay Now' button
// //
// //           payment: function() {
// //               // Set up the payment here
// //           },
// //
// //           onAuthorize: function(data, actions) {
// //               // Execute the payment here
// //          }
// //
// //       }, '#paypal-button');
// var CREATE_PAYMENT_URL  = 'https://my-store.com/paypal/create-payment';
//  var EXECUTE_PAYMENT_URL = 'https://my-store.com/paypal/execute-payment';
//
//      paypal.Button.render({
//
//          // Pass the client ids to use to create your transaction on sandbox and production environments
//
//          client: {
//              sandbox:    'access_token$sandbox$vzx5wr7p4y2s8kb2$fc998dfbb5635a8538bec05a17555769', // from https://developer.paypal.com/developer/applications/
//             //  production: 'xxxxxxxxx'  // from https://developer.paypal.com/developer/applications/
//          },
//
//          // Pass the payment details for your transaction
//          // See https://developer.paypal.com/docs/api/payments/#payment_create for the expected json parameters
//
//          payment: function(data, actions) {
//              return actions.payment.create({
//                  transactions: [
//                      {
//                          amount: {
//                              total:    '1.00',
//                              currency: 'USD'
//                          }
//                      }
//                  ]
//              });
//          },
//
//          // Display a "Pay Now" button rather than a "Continue" button
//
//          commit: true,
//
//          // Pass a function to be called when the customer completes the payment
//
//          onAuthorize: function(data, actions) {
//              return actions.payment.execute().then(function(response) {
//                  console.log('The payment was completed!');
//              });
//          },
// //
// //          // Pass a function to be called when the customer cancels the payment
// //
// //          onCancel: function(data) {
// //              console.log('The payment was cancelled!');
// //          }
// //  }, '#paypal-button');
// var CREATE_PAYMENT_URL  = 'https://my-store.com/paypal/create-payment';
//   var EXECUTE_PAYMENT_URL = 'https://my-store.com/paypal/execute-payment';
//
//   paypal.Button.render({
//
//       env: 'production', // Or 'sandbox'
//
//       commit: true, // Show a 'Pay Now' button
//
//       payment: function() {
//           return paypal.request.post(CREATE_PAYMENT_URL).then(function(data) {
//               return data.id;
//           });
//       },
//
//       onAuthorize: function(data) {
//           return paypal.request.post(EXECUTE_PAYMENT_URL, {
//               paymentID: data.paymentID,
//               payerID:   data.payerID
//           }).then(function() {
//
//               // The payment is complete!
//               // You can now show a confirmation message to the customer
//           });
//       }
//
//   }, '#paypal-button');
// paypal.Button.render({
//
//            env: 'sandbox', // sandbox | production
//
//            // PayPal Client IDs - replace with your own
//            // Create a PayPal app: https://developer.paypal.com/developer/applications/create
//            client: {
//                sandbox:    'AZDxjDScFpQtjWTOUtWKbyN_bDt4OgqaF4eYXlewfBP4-8aqX3PiV8e1GWU6liB2CUXlkA59kJXE7M6R',
//                production: 'AYIV-LTwqnn52pR-g-OHDhEp36DD3aw5PiKP866R3MVePcNg0NTSRgAUAbiUrZsyaJHv5o_L9fSOF3aA'
//            },
//
//            // Show the buyer a 'Pay Now' button in the checkout flow
//            commit: true,
//
//            // payment() is called when the button is clicked
//            payment: function(data, actions) {
//
//                // Make a call to the REST api to create the payment
//                return actions.payment.create({
//                    transactions: [
//                        {
//                            amount: { total: '0.01', currency: 'USD' }
//                        }
//                    ]
//                });
//            },
//
//            // onAuthorize() is called when the buyer approves the payment
//            onAuthorize: function(data, actions) {
//
//                // Make a call to the REST api to execute the payment
//                return actions.payment.execute().then(function() {
//                    window.alert('Payment Complete!');
//                });
//            }
//
//                   }, '#paypal-button-container');
// var CREATE_PAYMENT_URL  = 'https://my-store.com/paypal/create-payment';
//    var EXECUTE_PAYMENT_URL = 'https://my-store.com/paypal/execute-payment';
//
//    paypal.Button.render({
//
//        env: 'sandbox', // Or 'sandbox'
//
//        commit: true, // Show a 'Pay Now' button
//
//        payment: function() {
//            return paypal.request.post(CREATE_PAYMENT_URL).then(function(data) {
//                return data.id;
//               //  console.log(data.i)
//            });
//        },
//
//        onAuthorize: function(data) {
//            return paypal.request.post(EXECUTE_PAYMENT_URL, {
//                paymentID: data.paymentID,
//                payerID:   data.payerID
//            }).then(function() {
//
//                // The payment is complete!
//                // You can now show a confirmation message to the customer
//            });
//        }
//
//    }, '#paypal-button');
