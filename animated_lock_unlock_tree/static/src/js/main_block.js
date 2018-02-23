odoo.define('lock_unlock_tree.main_block', function(require) {
"use strict";
//Annadurai
var ListController = require('web.ListController');


ListController.include({_onButtonClicked: function (event) {
        event.stopPropagation();
        this._callButtonAction(event.data.attrs, event.data.record);
        if (event.data.attrs.name === 'action_done'){
        alertify.set('notifier','position', 'top-center');
        alertify.error("Locked "+event.data.record.data.name);
        }
        else if (event.data.attrs.name === 'action_unlock')
        alertify.success("UnLocked "+ event.data.record.data.name);
    },
        })
return ListController;

});
