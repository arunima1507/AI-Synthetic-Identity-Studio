let identityHistory = [];
let currentIdentity = null;
let generatedDataset = [];

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
        identityHistory.push(data);

        updateHistory();
        showIdentity(data);

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

function updateHistory() {

    const list = document.getElementById(
        "history-list"
    );

    list.innerHTML = "";

    identityHistory.forEach(
        (identity, index) => {

            const item =
                document.createElement("li");

            item.textContent =
                identity.profile.name;

            item.onclick = () => {

                showIdentity(identity);
            };

            list.appendChild(item);
        }
    );
}

function showIdentity(data) {

    currentIdentity = data;

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

function downloadJSON() {

    const dataStr =
        JSON.stringify(
            currentIdentity,
            null,
            4
        );

    const blob =
        new Blob(
            [dataStr],
            {
                type: "application/json"
            }
        );

    const url =
        URL.createObjectURL(blob);

    const a =
        document.createElement("a");

    a.href = url;

    a.download = "identity.json";

    a.click();

    URL.revokeObjectURL(url);
}

async function generateDataset(count) {

    generatedDataset = [];

    for(let i = 0; i < count; i++) {

        const response = await fetch(
            "http://127.0.0.1:8000/generate-identity"
        );

        const data = await response.json();

        generatedDataset.push(data);
    }

    updateDatasetStats();

    alert(
        `${count} identities generated`
    );
}

function downloadCSV() {

    if(generatedDataset.length === 0) {

        alert(
            "Generate a dataset first"
        );

        return;
    }

    let csv =
        "name,age,occupation,city,email,image_path\n";

    generatedDataset.forEach(
        identity => {

            csv +=
                `"${identity.profile.name}",` +
                `"${identity.profile.age}",` +
                `"${identity.profile.occupation}",` +
                `"${identity.profile.city}",` +
                `"${identity.profile.email}",` +
                `"${identity.image_path}"\n`;
        }
    );

    const blob =
        new Blob(
            [csv],
            {
                type: "text/csv"
            }
        );

    const url =
        URL.createObjectURL(blob);

    const a =
        document.createElement("a");

    a.href = url;

    a.download =
        "synthetic_dataset.csv";

    a.click();

    URL.revokeObjectURL(url);
}

function updateDatasetStats() {

    const count =
        generatedDataset.length;

    let totalAge = 0;

    const cities =
        new Set();

    const occupations =
        new Set();

    generatedDataset.forEach(
        identity => {

            totalAge +=
                identity.profile.age;

            cities.add(
                identity.profile.city
            );

            occupations.add(
                identity.profile.occupation
            );
        }
    );

    const avgAge =
        count > 0
        ? (totalAge / count).toFixed(1)
        : 0;

    document.getElementById(
        "dataset-size"
    ).textContent =
        `Dataset Size: ${count}`;

    document.getElementById(
        "avg-age"
    ).textContent =
        `Average Age: ${avgAge}`;

    document.getElementById(
        "unique-cities"
    ).textContent =
        `Unique Cities: ${cities.size}`;

    document.getElementById(
        "unique-occupations"
    ).textContent =
        `Unique Occupations: ${occupations.size}`;
}