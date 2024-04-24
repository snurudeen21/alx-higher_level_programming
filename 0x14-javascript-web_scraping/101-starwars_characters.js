const request = require('request');

function fetchCharacters() {
    const apiUrl = `https://swapi.dev/api/films/' + process.argv[2];

        request(apiUrl, (error, response, body) => {
        if (error) {
            console.error('Error:', error);
            return;
        }
        if (response.statusCode !== 200) {
            console.error('Unexpected status code:', response.statusCode);
            return;
        }

        const filmData = JSON.parse(body);

        const characters = filmData.characters;

        characters.forEach((characterUrl) => {
            request(characterUrl, (error, response, body) => {
                if (error) {
                    console.error('Error:', error);
                    return;
                }
                if (response.statusCode !== 200) {
                    console.error('Unexpected status code:', response.statusCode);
                    return;
                }

                const characterData = JSON.parse(body);
                console.log(characterData.name);
            });
        });
    });
}

fetchCharacters();
