(defproject algorithms-datastructures "0.1.0-SNAPSHOT"
  :description "FIXME: write description"
  :url "http://example.com/FIXME"
  :license {:name "GNU GPL v3+"
            :url "http://www.gnu.org/licenses/gpl-3.0.en.html"
            :addendum "GPL_ADDITION.md"}
  :github/private? false
  :dependencies [[camel-snake-kebab "0.4.2"]
                 [clj-time "0.15.2"]
                 [instaparse "1.4.11"]
                 [metosin/malli "0.8.4"]
                 [org.clojure/data.csv "1.0.1"]
                 [org.clojure/clojure "1.11.1"]]
  :target-path "target/%s"
  :profiles {:uberjar {:aot :all}})
