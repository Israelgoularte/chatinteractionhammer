function analisarIntencao() {
    // Obter a mensagem do usuário
    const mensagem = document.getElementById("mensagem").value;

    // Enviar a mensagem para o Python
    const xhr = new XMLHttpRequest();
    xhr.open("POST", "main.py");
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send(JSON.stringify({ mensagem }));

    // Exibir o resultado na tela
    xhr.onload = function() {
        const resultado = JSON.parse(xhr.responseText);
        document.getElementById("resultado").innerHTML = `
            <h2>Intenção detectada: ${resultado.intencao}</h2>
            <p>Informação extraída: ${resultado.informacao}</p>
        `;
    };
}
