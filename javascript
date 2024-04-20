fetch("https://trusttoken.dev/tt/(k,i,r)")
fetch("https://trusttoken.dev/tt/i?public={0,1,2,3,4,5,6}", {
    privateToken: {monstercoin} // Replace {...} with your private token object
}).then(addcoin);
fetch("https://trusttoken.dev/tt/r", {
    privateToken: {monstercoin} // Replace {...} with your private token object
}).then(addcoin);
fetch("https://your-redemption-record-endpoint", {
    privateToken: {monstercoin} // Replace {...} with your private token object
}).then(addcoin);
