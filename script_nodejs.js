const spawn = require("child_process").spawn

const pythonProcess = spawn("python", ["script_python"])

let pythonResponse = ""

pythonProcess.stdout.on("data", function(data){
    pythonResponse += data.toString()
})

pythonProcess.stdout.on("end", function(){
    console.log(pythonResponse)
})

pythonProcess.stdin.write("Entrada a procesar")

pythonProcess.stdin.end()






