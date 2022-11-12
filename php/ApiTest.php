<?php
require_once('../libvcwi.inc');
require_once('PHPUnit/Framework.php');

class ApiTest extends PHPUnit_Framework_TestCase
{
	protected $vc;

	protected $data = 0x01;
	protected $port = 50000;
	protected $len;

	protected function SetUp()
	{
		$this->$vc = new VCConnection();

		$this->$len = sizeof($this->$data);
	}

	public function testLogin()
	{
		$this->$vc->logIn('username', 'password');

		$this->markTestIncomplete();
	}

	public function testQuery()
	{
		$this->$vc->query('deviceid', 'key');

		$this->markTestIncomplete();
	}

	public function testSendBinary()
	{
		$this->$vc->sendBinary('target', $this->$port, $this->$len, 'type', 'comment');

		$this->markTestIncomplete();
	}

	public function testSendShortText()
	{
		$replyFlag = 'ON';
		$reply = $this->$vc->sendShortText('deviceid', $replyFlag, 'type', 'data', 'comment');

		$this->markTestIncomplete();
	}

	public function testRequestPDC()
	{
		$conn = $this->$vc->requestPDC('target', $this->$port, 'msg');

		$this->markTestIncomplete();
	}

	public function testRequestBinary()
	{
		$reply = $this->$vc->requestBinary('deviceid', $this->$port, 'key', 'msg');

		$this->markTestIncomplete();
	}

	public function testRequestShortText()
	{
		$this->$reply = $this->$vc->requestShortText('deviceid', 'key', 'msg');

		$this->markTestIncomplete();
	}

	public function testRequestShortTextStream()
	{
		$txtstream = $this->$vc->requestShortTextStream('deviceid', 'key', 'msg');
		$reply = $txtstream->getData();
		$reply = $txtstream->getData();
		$reply = $txtstream->getData();
		$reply = $txtstream->getData();
		$reply = $txtstream->getData();
		$txtstream->stop();

		$this->markTestIncomplete();
	}

	public function testRequestBaton()
	{
		$status = $this->$vc->requestBaton('deviceid', 'msg');

		$this->markTestIncomplete();
	}

	public function testReleaseBaton()
	{
		$this->$vc->releaseBaton('deviceid', 'msg');

		$this->markTestIncomplete();
	}

	public function testControl()
	{
		$this->$vc->control('deviceid', 'command', 'parameters');

		$this->markTestIncomplete();
	}

	public function testProxy()
	{
		$conn = $this->$vc->proxy($this->$port);

		$this->markTestIncomplete();
	}

	public function testSendRaw()
	{
		$reply = $this->$vc->sendRaw('rawpdu');

		$this->markTestIncomplete();
	}
}
?>