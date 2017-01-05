<!DOCTYPE HTML>
<html>
    <head>
        <meta charset="utf-8">
        <title>PAD</title>
    </head>
    <body>
        <h1>Students</h1>
        <table border="1">
          <thead>
            <td>#id</td>
            <td>name</td>
            <td>mark</td>
          </thead>
          <tbody>
            %for row in result:
              <tr>
                <td>{{row[0]}}</td>
                <td>{{row[1]}}</td>
                <td>{{row[2]}}</td>
              </tr>
            %end
          </tbody>
        </table>
    </body>
</html>
