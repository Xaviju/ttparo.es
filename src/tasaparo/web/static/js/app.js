(function() {
    var app = this.app;

    app.initialize = function() {
        if ($("#home-view").length > 0) {
            app.currentView = new Tasaparo.HomeView();
        } else if ($("#compare-view").length > 0) {
            app.currentView = new Tasaparo.CompateView();
        } else if ($("#map-view").length > 0) {
            app.currentView = new Tasaparo.MapView();
        } else if($("#profile-view").length > 0) {
            app.currentView = new Tasaparo.ProfileView();
        }
    };
}).call(this);

app.initialize.call(this);