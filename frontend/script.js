async function generateIdentity() {

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/generate-identity"
        );

        const data = await response.json();

        document.getElementById("identity-card").innerHTML = `
            <h2>${data.profile.name}</h2>

            <p>Age: ${data.profile.age}</p>

            <p>Occupation: ${data.profile.occupation}</p>

            <p>City: ${data.profile.city}</p>

            <p>Email: ${data.profile.email}</p>

            <p><b>Image:</b> ${data.image_path}</p>
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