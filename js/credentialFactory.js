#requires eris-contracts.js : https://github.com/eris-ltd/eris-contracts.js
var erisC = require('eris-contracts');

var erisdbURL = "http://localhost:1337/rpc";
var accountData = require('/some/account/data.json');
var contractManager = erisC.newContractManagerDev(erisdbURL, accountData);

var abi, compiled;
    try {
        abi = fs.readJsonSync('contracts/build/Credentials.abi');
        compiled = fs.readFileSync('contracts/build/Credentials.bin').toString();
    } catch (error){
        callback(error);
        return;
    }
    var credentialFactory = contractManager.newContractFactory(abi);

    credentialFactory.new({data: compiled}, function(error, contract){
        if(error){
            callback(error);
            return;
        }
    })
