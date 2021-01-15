function communicationExample() {
	// console.log(url);
	fetch(url)
		.then(response => response.json())
		.then(data => {
			let element = document.getElementById("contenu");
			
			const stripe = Stripe(stripePublicKey);
			stripe.redirectToCheckout({sessionId:data['session_id']})
		});
}