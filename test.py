# just ot test FritzHelper a bit outside domoticz


from fritzHelper import FritzHelper


def runTest(fh: FritzHelper):
    fh.dumpConfig()
    fh.readStatus()
    fh.dumpStatus()
    print("need Update: {}".format(fh.needUpdate))
    fh.readStatus()
    print("need Update: {}".format(fh.needUpdate))
    print("summary: {}".format(fh.getSummary()))
    print("summary short: {}".format(fh.getShortSummary()))
    print("summary short: {}".format(fh.getShortSummary("; ")))

    print("name:\t{}".format(fh.getDeviceName()))
    print("nameMB:\t{}".format(fh.getDeviceNameWithMB()))
    print("nameEIP:\t{}".format(fh.getDeviceNameWithEIP()))

    # print("date: {} level:{} txt: {} name: {}".format(y.getNearestDate(),
    #
    #                  y.getAlarmLevel(), y.getAlarmText(),
    #              y.getDeviceName()))
    #
fh = FritzHelper("fritz.box", "", "")
runTest(fh)