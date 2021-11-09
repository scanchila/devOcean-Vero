const COLORS = [
    '#4dc9f6',
    '#f67019',
    '#f53794',
    '#537bc4',
    '#acc236',
    '#166a8f',
    '#00a950',
    '#58595b',
    '#8549ba',
]

function color(index) {
    return COLORS[index % COLORS.length]
}

const CHART_COLORS = {
    red: 'rgb(255, 99, 132)',
    orange: 'rgb(255, 159, 64)',
    yellow: 'rgb(255, 205, 86)',
    green: 'rgb(75, 192, 192)',
    blue: 'rgb(54, 162, 235)',
    purple: 'rgb(153, 102, 255)',
    grey: 'rgb(201, 203, 207)',
}

const NAMED_COLORS = [
    CHART_COLORS.red,
    CHART_COLORS.orange,
    CHART_COLORS.yellow,
    CHART_COLORS.green,
    CHART_COLORS.blue,
    CHART_COLORS.purple,
    CHART_COLORS.grey,
]

// function transparentize(value, opacity) {
//     var alpha = opacity === undefined ? 0.5 : 1 - opacity
//     return colorLib(value).alpha(alpha).rgbString()
// }

function namedColor(index) {
    return NAMED_COLORS[index % NAMED_COLORS.length]
}

const chartActivities = new Chart(document.getElementById('chart-activities'), {
    type: 'bar',
    options: {
        responsive: true,
    },
})
const chartTypes = new Chart(document.getElementById('chart-types'), {
    type: 'doughnut',
    options: {
        responsive: true,
        parsing: {
            key: 'y',
        },
    },
})
const chartCategories = new Chart(document.getElementById('chart-categories'), {
    type: 'doughnut',
    options: {
        responsive: true,
        parsing: {
            key: 'y',
        },
    },
})

$(document).ready(async () => {
    const endpoint = 'http://127.0.0.1:8000/personalActivities/dashboard/info/'
    loadChart(chartActivities, endpoint + 'activities', 'activities')
    loadChart(chartTypes, endpoint + 'types', 'types')
    loadChart(chartCategories, endpoint + 'categories', 'categories')
})

const loadChart = async (chart, endpoint, chartName) => {
    data = await loadData(endpoint)
    if (data) {
        console.log(data)
        chart.data.datasets = []
        chart.data.labels = []
        chart.options.plugins.title.text = data.title
        chart.options.plugins.title.display = false
        chart.data.labels = data.data.labels
        data.data.datasets.forEach((dataset, i) => {
            let dsColor
            let dsBorder
            if (
                chart.options.type === 'pie' ||
                chart.options.type === 'doughnut'
            ) {
                dsColor = Object.values(CHART_COLORS)
                dsBorder = 'rgba(255, 255, 255, 0.9)'
            } else {
                dsColor = namedColor(i)
                dsBorder = dsColor
            }
            const ds = {
                ...dataset,
                backgroundColor: dsColor,
                borderColor: dsBorder,
                borderWidth: 1,
            }
            chart.data.datasets.push(ds)
        })
        chart.update()
        setControls(chart, chartName)
        console.log(chart.data)
    }
}

const loadData = async (endpoint) => {
    try {
        response = await $.ajax({
            url: endpoint,
            type: 'GET',
            dataType: 'json',
        })

        return response
    } catch (error) {
        return undefined
    }
}

const setControls = (chart, chartName) => {
    switchTotal = document.getElementById(chartName + '-hideTotal')
    switchTerm = document.getElementById(chartName + '-hideTerminadas')
    switchsinTerm = document.getElementById(chartName + '-hideSinTerminar')

    switchTotal.addEventListener('change', (event) => {
        if (event.currentTarget.checked) {
            chart.show(0)
        } else {
            chart.hide(0)
        }
    })

    switchsinTerm.addEventListener('change', (event) => {
        if (event.currentTarget.checked) {
            chart.show(1)
        } else {
            chart.hide(1)
        }
    })

    switchTerm.addEventListener('change', (event) => {
        if (event.currentTarget.checked) {
            chart.show(2)
        } else {
            chart.hide(2)
        }
    })
}
