(function (win, doc) {
    "use strict";

    document.addEventListener('DOMContentLoaded', function() {
        try {
            const labels = JSON.parse(document.getElementById('resourceTypeLabels').textContent);
            const data = JSON.parse(document.getElementById('resourceTypeData').textContent);

            const plotData = [{
                type: 'pie',
                labels: labels,
                values: data,
                textinfo: 'label+percent',
                insidetextorientation: 'radial'
            }];

            const layout = {
                title: 'Tipos de Recursos',
            };

            Plotly.newPlot('resourceChart', plotData, layout);
        } catch (e) {
            console.error("Erro ao processar os dados JSON:", e);
        }
    });

})(window, document);
