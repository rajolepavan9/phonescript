import org.boon.Boon;

def jsonEditorOptions = Boon.fromJson({
        disable_edit_json: true,
        disable_properties: true,
        no_additional_properties: true,
        disable_collapse: true,
        disable_array_add: true,
        disable_array_delete: true,
        disable_array_reorder: true,
        theme: "bootstrap2",
        iconlib:"fontawesome4",



	"phones":{
		"samsung":{
			"samsungmodel1":"j2"
			"samsungmodel2":"j4"
			"samsungmodel3":"j8"
			}
		"nokia":{
			"nokiamodel1":"1100"
			"nokiamodel2":"2200"
			"nokiamodel3":"3300"
			}
		"apple":{
			"applemodel1":"i4"
			"applemodel2":"i6"
			"applemodel3":"i10"
			}
		}
};
return jsonEditorOptions;
