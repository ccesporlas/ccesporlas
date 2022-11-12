<?php

	class command{


		private  $commandtype;
		private $parameter;
		private $numberOfparameters;
		private $commandTosend;
		private $TID;

		public function __construct($commandtype, array $params){

			$this->TID = rand();
			$this->commandtype = $commandtype;
			$this->parameter = $params;
			$this->numberOfparameters = count($params);

			for($i = 0; $i < $this->numberOfparameters-1; $i++) {
				$this->parameter[$i] = $this->parameter[$i]."|";
				$this->commandTosend = $this->commandTosend.$this->parameter[$i];
			}

			//echo "$this->commandTosend";
			$this->commandTosend = $this->commandTosend.$this->parameter[count($params)-1];
			$this->commandTosend = $this->TID." ".$this->commandtype." ".$this->commandTosend."\n";
			echo "$this->commandTosend";
		}

		public function getcommandtype(){
			return $this->commandtype;
		}

		public function getcommandTosend(){
			return $this->commandTosend;
		}

		public function getDID(){
			return $this->parameter[0];
		}

		public function getTID(){
			return $this->TID;
		}

		public function sendcommand(){
		 	$cc = stream_socket_client("tcp://127.0.0.1:41985", $errno, $errstr, 30);

			if (!$cc){
				echo "$errstr";
   			 	return;
			}
			echo "socket good";
			fwrite($cc, $this->commandTosend);

		}

		public function getreply(){

		}
}
?>