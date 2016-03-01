
// @GENERATOR:play-routes-compiler
// @SOURCE:/Users/keithy/Desktop/projects/Parsons-1/conf/routes
// @DATE:Tue Mar 01 13:18:08 EST 2016


package router {
  object RoutesPrefix {
    private var _prefix: String = "/"
    def setPrefix(p: String): Unit = {
      _prefix = p
    }
    def prefix: String = _prefix
    val byNamePrefix: Function0[String] = { () => prefix }
  }
}
