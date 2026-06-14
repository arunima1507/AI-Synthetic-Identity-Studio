async function generateIdentity() {

    document.getElementById("identity-card").innerHTML = `
        <h2>Generating Identity...</h2>
        <p>Please wait.</p>
    `;

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/generate-identity"
        );

        const data = await response.json();

        document.getElementById("identity-card").innerHTML = `
            <div class="card">

                <img
                    src="http://127.0.0.1:8000/${data.image_path}"
                    class="face-image"
                    alt="Generated Face"
                >

                <h2>${data.profile.name}</h2>

                <p><b>Age:</b> ${data.profile.age}</p>

                <p><b>Occupation:</b> ${data.profile.occupation}</p>

                <p><b>City:</b> ${data.profile.city}</p>

                <p><b>Email:</b> ${data.profile.email}</p>

                <button onclick="downloadCard()">
                    Download Identity Card
                </button>

            </div>
        `;
    }
    catch(error) {

        console.error(error);

        document.getElementById("identity-card").innerHTML = `
            <h2>Error</h2>
            <p>${error}</p>
        `;
    }
}

function downloadCard() {

    const card = document.getElementById("identity-card");

    const printWindow = window.open("", "_blank");

    printWindow.document.write(`
        <html>
        <head>
            <title>Identity Card</title>
        </head>
        <body>
            ${card.innerHTML}
        </body>
        </html>
    `);

    printWindow.document.close();

    printWindow.print();
}