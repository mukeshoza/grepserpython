import pandas as pd
import re

pd.set_option('display.max_rows', 1200)
pd.set_option('display.max_columns', 15)
pd.set_option('display.width', 1500)
pd.set_option('max_colwidth', 50)
pd.options.display.max_colwidth = 20000

placementgby = []
placementgby1 = []
placementgby2 = []
placementgby3 = []
indexappend = []
indexcount = []
spcountold = []
spcountnew = []
appendplac = []
appendold = []
appendnew = []
appenddiff = []
placcount = []
keywordcount = []
appendkey1 = []
appendkey2 = []
appendkey3 = []
appendkey4 = []
keycount = []
keywordcountnew = []
keycountnew = []
uniqueplacement = []
keywordallunique = []
key = []
keywordval = []
splitkey = []
splitkey1 = []
appendplacnew = []
appendcount = []
appendplac_new = []
appendplac_new1 = []
placcount_new = []
uniqueplacement1 = []
keywordallunique1 = []
key1 = []
keywordval1 = []
splitkey2 = []
splitkey3 = []
appendplacnew1 = []
appendcount1 = []
appendplac_new2 = []
appendplac_new3 = []
placcount_new1 = []
appendold1 = []
appendplac1 = []
placcount_old = []

filenameold = 'C:\myfiles\QA\grepserpython\generalscripts_python\\flywheel\\201907100911-Amazon-com-SOV-Base-2019-07-10.csv1\\201907100911-Amazon-com-SOV-Base-2019-07-10_1.csv'
filenamenew = 'C:\myfiles\QA\grepserpython\generalscripts_python\\flywheel\\201907100911-Amazon-com-SOV-Base-2019-07-10.csv1\\201907110216-Amazon-com-SOV-Base-2019-07-11_2.csv'

namefile = re.sub("\w+:\D\w+.*\\\\|.csv$", '', filenameold)
namefile1 = re.sub("\w+:\D\w+.*\\\\|.csv$", '', filenamenew)

if filenameold == '' and filenamenew != '':
    df1 = pd.read_csv(filenamenew, encoding='latin')

    totalcountnew = len(df1['ASIN'])
    placementnew = len(df1['Placement'])
    keywordnew = len(df1['Keyword'])
    placnew = df1['Placement']

    placegrp1 = df1.groupby(placnew).size().reset_index(name='count')
    for val1 in placegrp1['Placement']:
        placementgby2.append(val1)

    for val2 in placegrp1['count']:
        placementgby3.append(val2)

    data = list(zip(placementgby2, placementgby3))
    df3 = pd.DataFrame(data, columns=['Placement', 'count'])
    finalval = df3

    for plac in df3['Placement']:
        appendplac.append(plac)
    for plac1 in df3['count']:
        appendold.append(plac1)

    keynew = df1['Keyword']
    setkey = set(keynew)
    lenkey = len(setkey)
    grpnew = placnew.groupby(keynew).size().reset_index(name='count')

    df_plac = df1['Placement']
    df_key = df1['Keyword']

    for val_plac in df_plac:
        uniqueplacement.append(val_plac)

    unique_plac_grp = df1.groupby(uniqueplacement).size().reset_index(name='count')
    placindex = unique_plac_grp['index']
    placcountnew = unique_plac_grp['count']
    placindex_len = len(placindex)

    for valplacement, valkeyword in zip(df_plac, df_key):
        keywordallunique.append(valkeyword)

        for plac_val in range(0, placindex_len):
            try:
                if valplacement in placindex[plac_val]:
                    key.append((valplacement, valkeyword))
            except:
                continue

    abc = set(key)
    for valls in abc:
        splitkey.append(valls)
    dfnew = pd.DataFrame(splitkey)
    keyw = dfnew[0]
    plac = dfnew[1]
    unique_placement = dfnew.groupby(keyw).size().reset_index(name='count')
    for valplacnew in unique_placement[0]:
        appendplacnew.append(valplacnew)

    for valplacnew1 in unique_placement['count']:
        appendcount.append(valplacnew1)

    data_plac = list(zip(appendplacnew, appendcount))
    df_plac_new = pd.DataFrame(data_plac, columns=['Placement', 'count'])
    finalval_plac = df_plac_new

    for plac_new in df_plac_new['Placement']:
        appendplac_new.append(plac_new)
    for plac_new1 in df_plac_new['count']:
        appendplac_new1.append(plac_new1)

    for (valplac_new, valplac_new1, valplac_new2) in zip(appendplac_new, appendold, appendplac_new1):
        aplac_new = '<tr class = "table-secondary"><td scope="row">{}</td>'.format(valplac_new)
        bplac_new = '<td>{:,}</td>'.format(valplac_new1)
        cplac_new = '<td>{}</td>'.format(str(valplac_new2) + ' / ' + str(lenkey))
        avg = round(valplac_new2 / valplac_new1 * 100)
        dplac_new = '<td>{}%</td><tr>'.format(avg)

        valfinal = placcount_new.append(aplac_new)
        placcount_new.append(bplac_new)
        placcount_new.append(cplac_new)
        placcount_new.append(dplac_new)

    subplac_new = re.sub("\[|\]|\'|\,", '', str(placcount_new))
    final_plac_new = subplac_new

    # nettable = '''<a style = "margin-left:10%; margin-top:-8%;" class="btn btn-dark" data-toggle="collapse" href="#multiCollapseExample1" role="button" aria-expanded="false" aria-controls="multiCollapseExample1">Placement Per Keyword</a>
    #
    #    <div class="row">
    #      <div class="col">
    #        <div class="collapse multi-collapse" id="multiCollapseExample1">
    #          <table class="table table-hover">
    #      <table class="table table-hover" style="width:25%; margin-left:10%; margin-top:-1%">
    #      <thead>
    #        <tr>'''
    # tabnet1 = '<th scope="col" style="width:40%";>{}</th>'.format('Keyword')
    # tabnet2 = '<th scope="col" style="width:40%";>{}</th>'.format('Placement Count')
    #
    # tabnet3 = '''</tr></thead><tbody>'''
    #
    # val1 = grpnew['Keyword']
    # val2 = grpnew['count']
    #
    # for (val, vals) in zip(val1, val2):
    #     a = '<tr><td scope="row">{}</td>'.format(val)
    #     b = '<td>{}</td></tr>'.format(vals)
    #     ab = indexappend.append(a)
    #     indexappend.append(b)
    #
    # subnet = re.sub("\[|\]|\'|\,", '', str(indexappend))
    # finalsub = subnet
    #
    # tabnet4 = '''
    #      </tbody>
    #    </table></div></div></div>'''
    #
    # nettableall = nettable + tabnet1 + tabnet2 + tabnet3 + finalsub + tabnet4

    htmlcollapse = '''<!DOCTYPE html>
            <html>
            <head>
            <title>Flywheel Summary Report - Individual Report</title>
            <meta charset="utf-8">
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <script src = "https://cdn.jsdelivr.net/npm/chart.js@2.8.0/dist/Chart.min.js"></script></head>
            <body><p><hr><h3><center>Flywheel Summary Report - Individual Report</center></h3><hr></p>'''

    table = '''<div style = "margin-left:6%; margin-right:6%;"><table class="table table-hover">
              <thead>
                <tr class="bg-info">'''
    tab1 = '<th scope="col">{}</th><th scope="col"></th><th scope="col"></th>'.format('Fields')
    tab3 = '<th scope="col">{}</th>'.format('Count')
    table1 = tab1 + tab3

    tables = '''</tr>
              </thead>
              <tbody>
                <tr class = "table-light">'''

    tab5 = '<th scope="row">{}</th><th scope="col"></th><th scope="col"></th>'.format('Total Count')
    tab7 = '<td>{:,}</td></tr>'.format(totalcountnew)
    table2 = tab5 + tab7

    tabkey1 = '<tr class = "table-light"><th scope="row">{}</th><th scope="col"></th><th scope="col"></th>'.format(
        'Total Keywords')
    tabkey2 = '<td>{:,}</td></tr>'.format(lenkey)

    tabsp = '<tr class = "bg-info"><th scope="row">{}</th>'.format('Placement')
    tabsp1 = '<th scope="row">{}</th>'.format('Total Count')
    tabsp2 = '<th scope="row">{}</th>'.format('Keywords')
    tabsp3 = '<th scope="row">{}</th></tr>'.format('Average')

    tables2 = '''
              </tbody>
            </table></div>'''
    tableall = table + tables + table2 + tabkey1 + tabkey2 + tabsp + tabsp1 + tabsp2 + tabsp3 + final_plac_new + tables2

    statechart = '''<div style="float:left; width:50%; margin-top: 1%; margin-left: 30%; margin-bottom:3%;">
            <canvas id="myChart1" width="265" height="105"></canvas>
            <script>
            var ctx = document.getElementById('myChart1').getContext('2d');
            var myChart = new Chart(ctx, {
                type: 'pie',
                data: {
                    labels: '''
    datastate = placementgby2
    statevalues = ''',datasets: [{
            label: ['available count'],
            data: '''

    datacount1 = placementgby3

    remp1 = ''',
                        backgroundColor: [
                            'rgba(255, 99, 132, 0.8)',
                            'rgba(54, 162, 235, 0.8)',
                            'rgba(75, 192, 192, 0.8)',
                            'rgba(153, 102, 255, 0.8)',
                            'rgba(28, 130, 114, 0.8)',
                            'rgba(285, 108, 24, 0.8)',
                            'rgba(225, 180, 81, 0.8)',
                            'rgba(0, 34, 56, 0.8)',
                            'rgba(126, 245, 0, 0.8)',
                            'rgba(0, 245, 216, 0.8)',
                            'rgba(259, 99, 132, 0.8)'

                        ],
                        borderColor: [
                            'rgba(255, 99, 132, 0.8)',
                            'rgba(54, 162, 235, 0.8)',
                            'rgba(75, 192, 192, 0.8)',
                            'rgba(153, 102, 255, 0.8)',
                            'rgba(28, 130, 114, 0.8)',
                            'rgba(285, 108, 24, 0.8)',
                            'rgba(225, 180, 81, 0.8)',
                            'rgba(0, 34, 56, 0.8)',
                            'rgba(126, 245, 0, 0.8)',
                            'rgba(0, 245, 216, 0.8)',
                            'rgba(259, 99, 132, 0.8)'

                        ],
                        borderWidth: 2
                    }]
                },
                options: {
                    title: {
                        display: true,
                        fontsize: 14,
                        text: 'Placement Count'
                    },
                    legend: {
                        display: true,
                        position: 'right',
                        labels: {
                            generateLabels: function(chart) {
                                var data = chart.data;
                                if (data.labels.length && data.datasets.length) {
                                    return data.labels.map(function(label, i) {
                                        var meta = chart.getDatasetMeta(0);
                                        var ds = data.datasets[0];
                                        var arc = meta.data[i];
                                        var custom = arc && arc.custom || {};
                                        var getValueAtIndexOrDefault = Chart.helpers.getValueAtIndexOrDefault;
                                        var arcOpts = chart.options.elements.arc;
                                        var fill = custom.backgroundColor ? custom.backgroundColor : getValueAtIndexOrDefault(ds.backgroundColor, i, arcOpts.backgroundColor);
                                        var stroke = custom.borderColor ? custom.borderColor : getValueAtIndexOrDefault(ds.borderColor, i, arcOpts.borderColor);
                                        var bw = custom.borderWidth ? custom.borderWidth : getValueAtIndexOrDefault(ds.borderWidth, i, arcOpts.borderWidth);

                                        // We get the value of the current label
                                        var value = chart.config.data.datasets[arc._datasetIndex].data[arc._index];

                                        return {
                                            // Instead of `text: label,`
                                            // We add the value to the string
                                            text: label + " : " + value,
                                            fillStyle: fill,
                                            strokeStyle: stroke,
                                            lineWidth: bw,
                                            hidden: isNaN(ds.data[i]) || meta.data[i].hidden,
                                            index: i
                                        };
                                    });
                                } else {
                                    return [];
                                }
                            }
                        }
                    }
                }    


            });

            </script></div><br>'''
    statechatall = statechart + str(datastate) + statevalues + str(datacount1) + remp1
    statefinal = re.sub('data:\s+\[\(', 'data: [', statechatall)
    statefinalchart = re.sub('\)\]', ']', statefinal)

    all = '''
            <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
            <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>

            </body>
            </html>
            '''

    with open('flywheelreport_individual.html', 'w', buffering=9000000) as f:
        f.write(htmlcollapse + statefinalchart + tableall + all)
elif filenameold != '' and filenamenew == '':
    df1 = pd.read_csv(filenameold, encoding='latin')

    totalcountnew = len(df1['ASIN'])
    placementnew = len(df1['Placement'])
    keywordnew = len(df1['Keyword'])
    placnew = df1['Placement']

    placegrp1 = df1.groupby(placnew).size().reset_index(name='count')

    for val1 in placegrp1['Placement']:
        placementgby2.append(val1)

    for val2 in placegrp1['count']:
        placementgby3.append(val2)

    data = list(zip(placementgby2, placementgby3))
    df3 = pd.DataFrame(data, columns=['Placement', 'count'])
    finalval = df3

    for plac in df3['Placement']:
        appendplac.append(plac)
    for plac1 in df3['count']:
        appendold.append(plac1)

    keynew = df1['Keyword']
    setkey = set(keynew)
    lenkey = len(setkey)
    grpnew = placnew.groupby(keynew).size().reset_index(name='count')

    newnotsp = len(spcountnew)

    df_plac = df1['Placement']
    df_key = df1['Keyword']

    for val_plac in df_plac:
        uniqueplacement.append(val_plac)

    unique_plac_grp = df1.groupby(uniqueplacement).size().reset_index(name='count')
    placindex = unique_plac_grp['index']
    placcountnew = unique_plac_grp['count']
    placindex_len = len(placindex)

    for valplacement, valkeyword in zip(df_plac, df_key):
        keywordallunique.append(valkeyword)

        for plac_val in range(0, placindex_len):
            try:
                if valplacement in placindex[plac_val]:
                    key.append((valplacement, valkeyword))
            except:
                continue

    abc = set(key)
    for valls in abc:
        splitkey.append(valls)
    dfnew = pd.DataFrame(splitkey)
    keyw = dfnew[0]
    plac = dfnew[1]
    unique_placement = dfnew.groupby(keyw).size().reset_index(name='count')

    for valplacnew in unique_placement[0]:
        appendplacnew.append(valplacnew)

    for valplacnew1 in unique_placement['count']:
        appendcount.append(valplacnew1)

    data_plac = list(zip(appendplacnew, appendcount))
    df_plac_new = pd.DataFrame(data_plac, columns=['Placement', 'count'])
    finalval_plac = df_plac_new

    for plac_new in df_plac_new['Placement']:
        appendplac_new.append(plac_new)
    for plac_new1 in df_plac_new['count']:
        appendplac_new1.append(plac_new1)

    for (valplac_new, valplac_new1, valplac_new2) in zip(appendplac_new, appendold, appendplac_new1):
        aplac_new = '<tr class = "table-secondary"><td scope="row">{}</td>'.format(valplac_new)
        bplac_new = '<td>{:,}</td>'.format(valplac_new1)
        cplac_new = '<td>{}</td>'.format(str(valplac_new2) + ' / ' + str(lenkey))
        avg = round(valplac_new2 / valplac_new1 * 100)
        dplac_new = '<td>{}%</td><tr>'.format(avg)

        valfinal = placcount_new.append(aplac_new)
        placcount_new.append(bplac_new)
        placcount_new.append(cplac_new)
        placcount_new.append(dplac_new)

    subplac_new = re.sub("\[|\]|\'|\,", '', str(placcount_new))
    final_plac_new = subplac_new

    # nettable = '''<a style = "margin-left:10%; margin-top:-8%;" class="btn btn-dark" data-toggle="collapse" href="#multiCollapseExample1" role="button" aria-expanded="false" aria-controls="multiCollapseExample1">Placement Per Keyword</a>
    #
    #    <div class="row">
    #      <div class="col">
    #        <div class="collapse multi-collapse" id="multiCollapseExample1">
    #          <table class="table table-hover">
    #      <table class="table table-hover" style="width:25%; margin-left:10%; margin-top:-1%">
    #      <thead>
    #        <tr>'''
    # tabnet1 = '<th scope="col" style="width:40%";>{}</th>'.format('Keyword')
    # tabnet2 = '<th scope="col" style="width:40%";>{}</th>'.format('Placement Count')
    #
    # tabnet3 = '''</tr></thead><tbody>'''
    #
    # val1 = grpnew['Keyword']
    # val2 = grpnew['count']
    #
    # for (val, vals) in zip(val1, val2):
    #     a = '<tr><td scope="row">{}</td>'.format(val)
    #     b = '<td>{}</td></tr>'.format(vals)
    #     ab = indexappend.append(a)
    #     indexappend.append(b)
    #
    # subnet = re.sub("\[|\]|\'|\,", '', str(indexappend))
    # finalsub = subnet
    #
    # tabnet4 = '''
    #      </tbody>
    #    </table></div></div></div>'''
    #
    # nettableall = nettable + tabnet1 + tabnet2 + tabnet3 + finalsub + tabnet4

    htmlcollapse = '''<!DOCTYPE html>
        <html>
        <head>
        <title>Flywheel Summary Report - Individual Report</title>
        <meta charset="utf-8">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <script src = "https://cdn.jsdelivr.net/npm/chart.js@2.8.0/dist/Chart.min.js"></script></head>
        <body><p><hr><h3><center>Flywheel Summary Report - Individual Report</center></h3><hr></p>'''

    table = '''<div style = "margin-left:6%; margin-right:6%;"><table class="table table-hover">
          <thead>
            <tr class="bg-info">'''
    tab1 = '<th scope="col">{}</th><th scope="col"></th><th scope="col"></th>'.format('Fields')
    tab3 = '<th scope="col">{}</th>'.format('Count')
    table1 = tab1 + tab3

    tables = '''</tr>
          </thead>
          <tbody>
            <tr class = "table-light">'''

    tab5 = '<th scope="row">{}</th><th scope="col"></th><th scope="col"></th>'.format('Total Count')
    tab7 = '<td>{:,}</td></tr>'.format(totalcountnew)
    table2 = tab5 + tab7

    tabkey1 = '<tr class = "table-light"><th scope="row">{}</th><th scope="col"></th><th scope="col"></th>'.format(
        'Total Keywords')
    tabkey2 = '<td>{:,}</td></tr>'.format(lenkey)

    tabsp = '<tr class = "bg-info"><th scope="row">{}</th>'.format('Placement')
    tabsp1 = '<th scope="row">{}</th>'.format('Total Count')
    tabsp2 = '<th scope="row">{}</th>'.format('Keywords')
    tabsp3 = '<th scope="row">{}</th></tr>'.format('Average')

    tables2 = '''
          </tbody>
        </table></div>'''
    tableall = table + tables + table2 + tabkey1 + tabkey2 + tabsp + tabsp1 + tabsp2 + tabsp3 + final_plac_new + tables2

    statechart = '''<div style="float:left; width:50%; margin-top: 1%; margin-left: 30%; margin-bottom:3%;">
        <canvas id="myChart1" width="265" height="105"></canvas>
        <script>
        var ctx = document.getElementById('myChart1').getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'pie',
            data: {
                labels: '''
    datastate = placementgby2
    statevalues = ''',datasets: [{
        label: ['available count'],
        data: '''

    datacount1 = placementgby3

    remp1 = ''',
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.8)',
                        'rgba(54, 162, 235, 0.8)',
                        'rgba(75, 192, 192, 0.8)',
                        'rgba(153, 102, 255, 0.8)',
                        'rgba(28, 130, 114, 0.8)',
                        'rgba(285, 108, 24, 0.8)',
                        'rgba(225, 180, 81, 0.8)',
                        'rgba(0, 34, 56, 0.8)',
                        'rgba(126, 245, 0, 0.8)',
                        'rgba(0, 245, 216, 0.8)',
                        'rgba(259, 99, 132, 0.8)'

                    ],
                    borderColor: [
                        'rgba(255, 99, 132, 0.8)',
                        'rgba(54, 162, 235, 0.8)',
                        'rgba(75, 192, 192, 0.8)',
                        'rgba(153, 102, 255, 0.8)',
                        'rgba(28, 130, 114, 0.8)',
                        'rgba(285, 108, 24, 0.8)',
                        'rgba(225, 180, 81, 0.8)',
                        'rgba(0, 34, 56, 0.8)',
                        'rgba(126, 245, 0, 0.8)',
                        'rgba(0, 245, 216, 0.8)',
                        'rgba(259, 99, 132, 0.8)'

                    ],
                    borderWidth: 2
                }]
            },
            options: {
                title: {
                    display: true,
                    fontsize: 14,
                    text: 'Placement Count'
                },
                legend: {
                    display: true,
                    position: 'right',
                    labels: {
                        generateLabels: function(chart) {
                            var data = chart.data;
                            if (data.labels.length && data.datasets.length) {
                                return data.labels.map(function(label, i) {
                                    var meta = chart.getDatasetMeta(0);
                                    var ds = data.datasets[0];
                                    var arc = meta.data[i];
                                    var custom = arc && arc.custom || {};
                                    var getValueAtIndexOrDefault = Chart.helpers.getValueAtIndexOrDefault;
                                    var arcOpts = chart.options.elements.arc;
                                    var fill = custom.backgroundColor ? custom.backgroundColor : getValueAtIndexOrDefault(ds.backgroundColor, i, arcOpts.backgroundColor);
                                    var stroke = custom.borderColor ? custom.borderColor : getValueAtIndexOrDefault(ds.borderColor, i, arcOpts.borderColor);
                                    var bw = custom.borderWidth ? custom.borderWidth : getValueAtIndexOrDefault(ds.borderWidth, i, arcOpts.borderWidth);

                                    // We get the value of the current label
                                    var value = chart.config.data.datasets[arc._datasetIndex].data[arc._index];

                                    return {
                                        // Instead of `text: label,`
                                        // We add the value to the string
                                        text: label + " : " + value,
                                        fillStyle: fill,
                                        strokeStyle: stroke,
                                        lineWidth: bw,
                                        hidden: isNaN(ds.data[i]) || meta.data[i].hidden,
                                        index: i
                                    };
                                });
                            } else {
                                return [];
                            }
                        }
                    }
                }
            }    


        });

        </script></div><br>'''
    statechatall = statechart + str(datastate) + statevalues + str(datacount1) + remp1
    statefinal = re.sub('data:\s+\[\(', 'data: [', statechatall)
    statefinalchart = re.sub('\)\]', ']', statefinal)

    all = '''
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>

        </body>
        </html>
        '''

    with open('flywheelreport_individual.html', 'w', buffering=9000000) as f:
        f.write(htmlcollapse + statefinalchart + tableall + all)

###comparativereport###

if filenameold != '' and filenamenew != '':
    df = pd.read_csv(filenameold, encoding='latin')
    df1 = pd.read_csv(filenamenew, encoding='latin')

    # totalcountold = len(df['Keyword'])
    # totalcountnew = len(df1['Keyword'])

    placementold = len(df['Placement'])
    placementnew = len(df1['Placement'])

    keywordold = len(df['Keyword'])
    keywordnew = len(df1['Keyword'])

    placold = df['Placement']
    placnew = df1['Placement']
    placegrp = df.groupby(placold).size().reset_index(name='count')
    placegrp1 = df1.groupby(placnew).size().reset_index(name='count')

    for values in placegrp['Placement']:
        placementgby.append(values)

    for val in placegrp['count']:
        placementgby1.append(val)

    for val1 in placegrp1['Placement']:
        placementgby2.append(val1)

    for val2 in placegrp1['count']:
        placementgby3.append(val2)

    placegrp1 = df1.groupby(placold).size().reset_index(name='count')

    data_1 = list(zip(placementgby, placementgby1))
    df4 = pd.DataFrame(data_1, columns=['Placement', 'count'])
    finalval_1 = df4

    for plac_2 in df4['Placement']:
        appendplac1.append(plac_2)
    for plac_3 in df4['count']:
        appendold1.append(plac_3)

    placegrp2 = df1.groupby(placnew).size().reset_index(name='count')

    data = list(zip(placementgby2, placementgby3))
    df3 = pd.DataFrame(data, columns=['Placement', 'count'])
    finalval = df3

    for plac in df3['Placement']:
        appendplac.append(plac)
    for plac1 in df3['count']:
        appendold.append(plac1)

    keynew = df1['Keyword']
    setkey = set(keynew)
    lenkey = len(setkey)

    keyold = df['Keyword']
    setkeyold = set(keyold)
    lenkeyold = len(setkeyold)

    grpnew = placnew.groupby(keynew).size().reset_index(name='count')

    df_plac = df1['Placement']
    df_plac1 = df['Placement']
    df_key1 = df['Keyword']
    df_key = df1['Keyword']

    for val_plac in df_plac:
        uniqueplacement.append(val_plac)

    unique_plac_grp = df1.groupby(uniqueplacement).size().reset_index(name='count')
    placindex = unique_plac_grp['index']
    placcountnew = unique_plac_grp['count']
    placindex_len = len(placindex)

    for valplacement, valkeyword in zip(df_plac, df_key):
        keywordallunique.append(valkeyword)

        for plac_val in range(0, placindex_len):
            try:
                if valplacement in placindex[plac_val]:
                    key.append((valplacement, valkeyword))
            except:
                continue

    abc = set(key)
    for valls in abc:
        splitkey.append(valls)
    dfnew = pd.DataFrame(splitkey)
    keyw = dfnew[0]
    plac = dfnew[1]
    unique_placement = dfnew.groupby(keyw).size().reset_index(name='count')

    for valplacnew in unique_placement[0]:
        appendplacnew.append(valplacnew)

    for valplacnew1 in unique_placement['count']:
        appendcount.append(valplacnew1)

    data_plac = list(zip(appendplacnew, appendcount))
    df_plac_new = pd.DataFrame(data_plac, columns=['Placement', 'count'])
    finalval_plac = df_plac_new

    for plac_new in df_plac_new['Placement']:
        appendplac_new.append(plac_new)
    for plac_new1 in df_plac_new['count']:
        appendplac_new1.append(plac_new1)

    for (valplac_new, valplac_new1, valplac_new2) in zip(appendplac_new, appendold, appendplac_new1):
        aplac_new = '<tr class = "table-secondary"><td scope="row">{}</td>'.format(valplac_new)
        bplac_new = '<td>{:,}</td>'.format(valplac_new1)
        cplac_new = '<td>{}</td>'.format(str(valplac_new2) + ' / ' + str(lenkey))
        avg = round(valplac_new2 / valplac_new1 * 100)
        dplac_new = '<td>{}%</td><tr>'.format(avg)

        valfinal = placcount_new.append(aplac_new)
        placcount_new.append(bplac_new)
        placcount_new.append(cplac_new)
        placcount_new.append(dplac_new)

    subplac_new = re.sub("\[|\]|\'|\,", '', str(placcount_new))
    final_plac_new = subplac_new

    ##########################secondtable#########################

    for val_plac1 in df_plac1:
        uniqueplacement1.append(val_plac1)

    unique_plac_grp1 = df.groupby(uniqueplacement1).size().reset_index(name='count')
    placindex1 = unique_plac_grp1['index']
    placcountnew_1 = unique_plac_grp1['count']
    placindex_len1 = len(placindex1)

    for valplacement1, valkeyword1 in zip(df_plac1, df_key1):
        keywordallunique1.append(valkeyword1)

        for plac_val1 in range(0, placindex_len1):
            try:
                if valplacement1 in placindex1[plac_val1]:
                    key1.append((valplacement1, valkeyword1))
            except:
                continue

    abc1 = set(key1)
    for valls1 in abc1:
        splitkey1.append(valls1)
    dfnew1 = pd.DataFrame(splitkey1)
    keyw1 = dfnew1[0]
    plac_1 = dfnew1[1]
    unique_placement1 = dfnew.groupby(keyw1).size().reset_index(name='count')

    for valplacnew_1 in unique_placement1[0]:
        appendplacnew1.append(valplacnew_1)

    for valplacnew_2 in unique_placement1['count']:
        appendcount1.append(valplacnew_2)

    data_plac1 = list(zip(appendplacnew1, appendcount1))
    df_plac_new1 = pd.DataFrame(data_plac1, columns=['Placement', 'count'])
    finalval_plac1 = df_plac_new1

    for plac_new_1 in df_plac_new1['Placement']:
        appendplac_new2.append(plac_new_1)
    for plac_new_2 in df_plac_new1['count']:
        appendplac_new3.append(plac_new_2)

    for (valplac_old, valplac_old1, valplac_old2) in zip(appendplac_new2, appendold1, appendplac_new3):
        aplac_old = '<tr class = "table-secondary"><td scope="row">{}</td>'.format(valplac_old)
        bplac_old = '<td>{:,}</td>'.format(valplac_old1)
        cplac_old = '<td>{}</td>'.format(str(valplac_old2) + ' / ' + str(lenkeyold))
        avg1 = round(valplac_old2 / valplac_old1 * 100)
        dplac_old = '<td>{}%</td><tr>'.format(avg1)

        valfinal1 = placcount_old.append(aplac_old)
        placcount_old.append(bplac_old)
        placcount_old.append(cplac_old)
        placcount_old.append(dplac_old)

    subplac_new1 = re.sub("\[|\]|\'|\,", '', str(placcount_old))
    final_plac_new1 = subplac_new1

    ##############End Secon Table#################

    htmlcollapse = '''<!DOCTYPE html>
        <html>
        <head>
        <title>Flywheel Summary Report - Comparative Report</title>
        <meta charset="utf-8">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <script src = "https://cdn.jsdelivr.net/npm/chart.js@2.8.0/dist/Chart.min.js"></script></head>
        <body><p><hr><h3><center>Flywheel Summary Report - Comparative Report</center></h3><hr></p>'''

    table = '''<div style = "margin-right:3%; float:right; width:40%;"><table class="table table-hover"><br><h4 style = "margin-left:40%;">New Report</h4>
                  <thead>
                    <tr class="bg-info">'''

    tab5 = '<tr class = "table-light" style="margin-bottom:5%;"><th scope="row">{}</th><th scope="col"></th><th scope="col"></th>'.format(
        'Total Count')
    tab7 = '<td>{:,}</td></tr>'.format(keywordnew)
    table2 = tab5 + tab7

    tabkey1 = '<tr class = "table-light"><th scope="row">{}</th><th scope="col"></th><th scope="col"></th>'.format(
        'Total Keywords')
    tabkey2 = '<td>{:,}</td></tr>'.format(lenkey)

    tabsp = '<tr class = "bg-info"><th scope="row">{}</th>'.format('Placement')
    tabsp1 = '<th scope="row">{}</th>'.format('Total Count')
    tabsp2 = '<th scope="row">{}</th>'.format('Keywords')
    tabsp3 = '<th scope="row">{}</th></tr>'.format('Average')

    tables2 = '''
                  </tbody>
                </table></div>'''
    tableall = table + table2 + tabkey1 + tabkey2 + tabsp + tabsp1 + tabsp2 + tabsp3 + final_plac_new + tables2

    #####Table Second####

    tableold = '''<div style = "margin-left:3%; float:left; width:40%;"><table class="table table-hover"><br><h4 style = "margin-left:40%;">Old Report</h4>
                     <thead>
                       <tr class="bg-info">'''

    tab5old = '<tr class = "table-light" style="margin-bottom:5%;"><th scope="row">{}</th><th scope="col"></th><th scope="col"></th>'.format(
        'Total Count')
    tab7old = '<td>{:,}</td></tr>'.format(keywordold)
    table2old = tab5old + tab7old

    tabkey1old = '<tr class = "table-light"><th scope="row">{}</th><th scope="col"></th><th scope="col"></th>'.format(
        'Total Keywords')
    tabkey2old = '<td>{:,}</td></tr>'.format(lenkeyold)

    tabspold = '<tr class = "bg-info"><th scope="row">{}</th>'.format('Placement')
    tabsp1old = '<th scope="row">{}</th>'.format('Total Count')
    tabsp2old = '<th scope="row">{}</th>'.format('Keywords')
    tabsp3old = '<th scope="row">{}</th></tr>'.format('Average')

    tables2old = '''
                     </tbody>
                   </table></div>'''
    tableallold = tableold + table2old + tabkey1old + tabkey2old + tabspold + tabsp1old + tabsp2old + tabsp3old + final_plac_new1 + tables2old

    #####End Table Second####

    provchart = '''<div><div style= "float: left; width:40%; margin-top: 0%; margin-left: 5%;">
    <canvas id="myChart2" width="240" height="100"></canvas>
    <script>
    var ctx = document.getElementById('myChart2').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: '''
    datanet = placementgby
    datavalues = ''',datasets: [{
    label: ['available count'],
    data: '''

    datacount = placementgby1

    remp = ''',
                backgroundColor: [
                    'rgba(255, 99, 132, 0.8)',
                    'rgba(54, 162, 235, 0.8)',
                    'rgba(75, 192, 192, 0.8)',
                    'rgba(153, 102, 255, 0.8)',
                    'rgba(28, 130, 114, 0.8)',
                    'rgba(285, 108, 24, 0.8)',
                    'rgba(225, 180, 81, 0.8)',
                    'rgba(0, 34, 56, 0.8)',
                    'rgba(126, 245, 0, 0.8)',
                    'rgba(0, 245, 216, 0.8)',
                    'rgba(259, 99, 132, 0.8)'

                ],
                borderColor: [
                    'rgba(255, 99, 132, 0.8)',
                    'rgba(54, 162, 235, 0.8)',
                    'rgba(75, 192, 192, 0.8)',
                    'rgba(153, 102, 255, 0.8)',
                    'rgba(28, 130, 114, 0.8)',
                    'rgba(285, 108, 24, 0.8)',
                    'rgba(225, 180, 81, 0.8)',
                    'rgba(0, 34, 56, 0.8)',
                    'rgba(126, 245, 0, 0.8)',
                    'rgba(0, 245, 216, 0.8)',
                    'rgba(259, 99, 132, 0.8)'

                ],
                borderWidth: 2
            }]
        },
        options: {
            title: {
                display: true,
                fontsize: 14,
                text: 'Placement Old Count'
            },
            legend: {
                display: true,
                position: 'right',
                labels: {
                    generateLabels: function(chart) {
                        var data = chart.data;
                        if (data.labels.length && data.datasets.length) {
                            return data.labels.map(function(label, i) {
                                var meta = chart.getDatasetMeta(0);
                                var ds = data.datasets[0];
                                var arc = meta.data[i];
                                var custom = arc && arc.custom || {};
                                var getValueAtIndexOrDefault = Chart.helpers.getValueAtIndexOrDefault;
                                var arcOpts = chart.options.elements.arc;
                                var fill = custom.backgroundColor ? custom.backgroundColor : getValueAtIndexOrDefault(ds.backgroundColor, i, arcOpts.backgroundColor);
                                var stroke = custom.borderColor ? custom.borderColor : getValueAtIndexOrDefault(ds.borderColor, i, arcOpts.borderColor);
                                var bw = custom.borderWidth ? custom.borderWidth : getValueAtIndexOrDefault(ds.borderWidth, i, arcOpts.borderWidth);

                                // We get the value of the current label
                                var value = chart.config.data.datasets[arc._datasetIndex].data[arc._index];

                                return {
                                    // Instead of `text: label,`
                                    // We add the value to the string
                                    text: label + " : " + value,
                                    fillStyle: fill,
                                    strokeStyle: stroke,
                                    lineWidth: bw,
                                    hidden: isNaN(ds.data[i]) || meta.data[i].hidden,
                                    index: i
                                };
                            });
                        } else {
                            return [];
                        }
                    }
                }
            }
        }

    });

    </script></div></div>'''
    allchartp = provchart + str(datanet) + datavalues + str(datacount) + remp
    finaldatap = re.sub('data:\s+\[\(', 'data: [', allchartp)
    finalchartp = re.sub('\)\]', ']', finaldatap)

    statechart = '''<div style="float:right; width:45%; margin-top: 0; margin-right:5%;">
    <canvas id="myChart1" width="265" height="100"></canvas>
    <script>
    var ctx = document.getElementById('myChart1').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: '''
    datastate = placementgby2
    statevalues = ''',datasets: [{
    label: ['available count'],
    data: '''

    datacount1 = placementgby3

    remp1 = ''',
                backgroundColor: [
                    'rgba(255, 99, 132, 0.8)',
                    'rgba(54, 162, 235, 0.8)',
                    'rgba(75, 192, 192, 0.8)',
                    'rgba(153, 102, 255, 0.8)',
                    'rgba(28, 130, 114, 0.8)',
                    'rgba(285, 108, 24, 0.8)',
                    'rgba(225, 180, 81, 0.8)',
                    'rgba(0, 34, 56, 0.8)',
                    'rgba(126, 245, 0, 0.8)',
                    'rgba(0, 245, 216, 0.8)',
                    'rgba(259, 99, 132, 0.8)'

                ],
                borderColor: [
                    'rgba(255, 99, 132, 0.8)',
                    'rgba(54, 162, 235, 0.8)',
                    'rgba(75, 192, 192, 0.8)',
                    'rgba(153, 102, 255, 0.8)',
                    'rgba(28, 130, 114, 0.8)',
                    'rgba(285, 108, 24, 0.8)',
                    'rgba(225, 180, 81, 0.8)',
                    'rgba(0, 34, 56, 0.8)',
                    'rgba(126, 245, 0, 0.8)',
                    'rgba(0, 245, 216, 0.8)',
                    'rgba(259, 99, 132, 0.8)'

                ],
                borderWidth: 2
            }]
        },
        options: {
            title: {
                display: true,
                fontsize: 14,
                text: 'Placement New Count'
            },
            legend: {
                display: true,
                position: 'right',
                labels: {
                    generateLabels: function(chart) {
                        var data = chart.data;
                        if (data.labels.length && data.datasets.length) {
                            return data.labels.map(function(label, i) {
                                var meta = chart.getDatasetMeta(0);
                                var ds = data.datasets[0];
                                var arc = meta.data[i];
                                var custom = arc && arc.custom || {};
                                var getValueAtIndexOrDefault = Chart.helpers.getValueAtIndexOrDefault;
                                var arcOpts = chart.options.elements.arc;
                                var fill = custom.backgroundColor ? custom.backgroundColor : getValueAtIndexOrDefault(ds.backgroundColor, i, arcOpts.backgroundColor);
                                var stroke = custom.borderColor ? custom.borderColor : getValueAtIndexOrDefault(ds.borderColor, i, arcOpts.borderColor);
                                var bw = custom.borderWidth ? custom.borderWidth : getValueAtIndexOrDefault(ds.borderWidth, i, arcOpts.borderWidth);

                                // We get the value of the current label
                                var value = chart.config.data.datasets[arc._datasetIndex].data[arc._index];

                                return {
                                    // Instead of `text: label,`
                                    // We add the value to the string
                                    text: label + " : " + value,
                                    fillStyle: fill,
                                    strokeStyle: stroke,
                                    lineWidth: bw,
                                    hidden: isNaN(ds.data[i]) || meta.data[i].hidden,
                                    index: i
                                };
                            });
                        } else {
                            return [];
                        }
                    }
                }
            }
        }    


    });

    </script></div><br>'''
    statechatall = statechart + str(datastate) + statevalues + str(datacount1) + remp1
    statefinal = re.sub('data:\s+\[\(', 'data: [', statechatall)
    statefinalchart = re.sub('\)\]', ']', statefinal)

    all = '''
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>

    </body>
    </html>
    '''

    with open('flywheelreport_comparative_old_new.html', 'w', buffering=9000000) as f:
        f.write(htmlcollapse + finalchartp + statefinalchart + tableallold + tableall + all)
else:
    pass

