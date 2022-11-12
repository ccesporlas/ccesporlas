<?php

include('command.php');
include('clientsession.php');

//$cmdtype = $_GET['CMDTYPE'];
//$params = $_GET['PARAMS'];

print "touch";

$cmdtype = "LOGIN";
$params = array(0=>TEST,1=>TEST);

$cmd = new $command($cmdtype,$params);
client_handler $session;
$cmdTosend = $cmd->getcommandTosend();

if (!($session->isloggedin()) and ($cmd->getcommandtype !="LOGIN")) {

	    echo "NOT LOGGED IN YET";
	    return;
}

else {

	if ($cmd) {
	//create and open CC
		$cc = stream_socket_client("tcp://127.0.0.1:42015", $errno, $errstr, 30);
    		if (!$cc) {
        		echo "$errstr";
            		return;
              	}
		
		fwrite($cc, $cmddToSend . " \n");
		echo "waiting reply";
		return;
	}
	
	if (!$cmd){
		echo "no command";
		return;
		}
}  

?>