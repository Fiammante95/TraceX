from opcua import ua, Server

# setup our server
server = Server()
server.set_endpoint("opc.tcp://192.168.8.211:4840/tracex/sim/")
server.set_server_name("traceX simulation OPC-UA server")
# setup our own namespace, not really necessary but should as spec
# set all possible endpoint policies for clients to connect through
server.set_security_policy([
    ua.SecurityPolicyType.NoSecurity,
    ua.SecurityPolicyType.Basic256Sha256_SignAndEncrypt,
    ua.SecurityPolicyType.Basic256Sha256_Sign])

uri = "http://CoBot.opcua.server"
idx = server.register_namespace(uri)
# get Objects node, this is where we should put our custom stuff
#
objects = server.get_objects_node()
# populating our address space
#
electricData = objects.add_object(idx, "CobotElectricData")
voltageM1 = electricData.add_variable(idx, "voltageM1", ua.Variant(0, ua.VariantType.Float))
voltageM2 = electricData.add_variable(idx, "voltageM2", ua.Variant(0, ua.VariantType.Float))
voltageM3 = electricData.add_variable(idx, "voltageM3", ua.Variant(0, ua.VariantType.Float))
voltageM4 = electricData.add_variable(idx, "voltageM4", ua.Variant(0, ua.VariantType.Float))
voltageM5 = electricData.add_variable(idx, "voltageM5", ua.Variant(0, ua.VariantType.Float))
voltageLED = electricData.add_variable(idx, "voltageLED", ua.Variant(0, ua.VariantType.Float))

state = objects.add_object(idx, "CobotState")
processStep = state.add_variable(idx, "processState", ua.Variant(0, ua.VariantType.Double))
# starting!
server.start()

voltageM1.set_value(0)
