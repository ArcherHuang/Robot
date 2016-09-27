var Translate = require('@google-cloud/translate');

var translate = Translate({
    key: "<<Input Key>>"
  });

translate.detect('Hello', function (err, result) {
    if (err) {
      
    }

    console.log('Detected language(s):', result);
  });
