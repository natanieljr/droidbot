import logging
import random
from wekapy import *
from valid_widgets import get_refined_type


class ModelBased(object):
    @staticmethod
    def add_instance(model, item):
        test_instance = Instance()

        refined_type = get_refined_type(item["class"])
        parent = get_refined_type(item["parent"])
        children1 = get_refined_type(item["children1"])
        children2 = get_refined_type(item["children2"])

        test_instance.add_features([Feature(name="RefinedType", value=refined_type, possible_values="{linearlayout,togglebutton,actionbarcontextview,menu,textview,relativelayout,scrollview,imageview,edittext,framelayout,checkedtextview,button,imagebutton,progressbar,view,baselinelayout,nestedscrollview,item,autocompletetextview,appcompatbutton,linearlayoutics,checkbox,viewanimator,spinner,actionbarview,floatingactionbutton,navigationmenuitemview,fitwindowslinearlayout,viewpager,textureview,horizontalscrollview,actionbaroverlaylayout,chronometer,webview,tintimageview,actionmenuitemview,viewstub,preferenceimageview,viewstubcompat,contentframelayout,tablerow,switch,actionmenuview,listmenuitemview,appcompatradiobutton,radiobutton,listview,coordinatorlayout,appcompattextview,seekbar,actionbarcontainer,cardview,textinputlayout,navigationmenuview,gridview,radiogroup,dialogtitle,toolbar,space,recyclerview,ratingbar,datepicker,expandedmenuview,datetimeview,expandablelistview,surfaceview,navigationview,slidingdrawer,viewswitcher,unpressablelinearlayout,switchcompat,buttonbarlayout,appcompatspinner,numberpicker,tablelayout,gridlayout,viewflipper,tablayout,fitwindowsframelayout,checkableimagebutton,listpreference,linearlayoutcompat,appbarlayout,calendarview,swiperefreshlayout,searchview,imageswitcher,pagertabstrip,appcompatimageview,fragmenttabhost,videoview,checkboxpreference,preferencescreen,appcompatcheckbox,textviewwrapper,tabwidget,drawerlayout,timepicker,textswitcher,preferencecategory,gallery,tabhost,preference,pagertitlestrip,absolutelayout,alertdialoglayout,analogclock,collapsingtoolbarlayout}"),
                                     Feature(name="Parent1", value=parent, possible_values="{item,none,framelayout,linearlayout,tablerow,actionbaroverlaylayout,menu,relativelayout,buttonbarlayout,listmenuitemview,textinputlayout,view,checkedtextview,cardview,preferenceimageview,fitwindowslinearlayout,viewpager,fitwindowsframelayout,collapsingtoolbarlayout,linearlayoutcompat,tablelayout,scrollview,radiogroup,progressbar,contentframelayout,horizontalscrollview,actionbarcontainer,alertdialoglayout,expandablelistview,actionbarview,navigationview,textview,coordinatorlayout,gridlayout,toolbar,viewswitcher,unpressablelinearlayout,surfaceview,recyclerview,floatingactionbutton,swiperefreshlayout,nestedscrollview,imageview,preferencecategory,group,actionmenuitemview,viewflipper,baselinelayout,listview,datetimeview,navigationmenuview,preferencescreen,drawerlayout,appbarlayout,seekbar,actionmenuview,calendarview,appcompatimageview,gridview,ratingbar,fragmenttabhost,actionbarcontextview,imageswitcher,checkableimagebutton,expandedmenuview,textureview,videoview,viewstub,slidingdrawer,tabhost,dialogtitle,gallery,viewanimator,tintimageview,switchcompat,chronometer,webview,absolutelayout,tabwidget,appcompattextview,textviewwrapper,listpreference,textswitcher,togglebutton,navigationmenuitemview,imagebutton,button,autocompletetextview,searchview,pagertabstrip,edittext,checkbox,tablayout,space,preference,analogclock,switch,timepicker,spinner,appcompatspinner,checkboxpreference}"),
                                     Feature(name="Children1", value=children1, possible_values="{view,none,item,button,linearlayout,actionbarcontextview,menu,relativelayout,framelayout,textview,surfaceview,checkbox,imageview,progressbar,checkedtextview,scrollview,appbarlayout,viewstub,imagebutton,pagertabstrip,listview,seekbar,edittext,viewpager,datetimeview,cardview,swiperefreshlayout,listmenuitemview,space,tintimageview,radiobutton,autocompletetextview,nestedscrollview,toolbar,buttonbarlayout,actionbarview,coordinatorlayout,contentframelayout,actionbarcontainer,webview,appcompattextview,gridview,appcompatbutton,viewanimator,radiogroup,textinputlayout,preferenceimageview,fitwindowslinearlayout,togglebutton,floatingactionbutton,tablerow,appcompatimageview,viewstubcompat,tablelayout,spinner,horizontalscrollview,actionmenuview,numberpicker,textureview,textviewwrapper,tablayout,videoview,preferencescreen,group,recyclerview,imageswitcher,actionmenuitemview,timepicker,calendarview,switchcompat,expandablelistview,chronometer,gallery,ratingbar,baselinelayout,pagertitlestrip,tabwidget,searchview,unpressablelinearlayout,datepicker,appcompatradiobutton,switch,navigationview,checkboxpreference,listpreference,collapsingtoolbarlayout,preference,viewflipper,checkableimagebutton,expandedmenuview,slidingdrawer,appcompatspinner,gridlayout,actionbaroverlaylayout,fragmenttabhost,navigationmenuview,tabhost,dialogtitle,drawerlayout,preferencecategory,viewswitcher,navigationmenuitemview,alertdialoglayout,linearlayoutcompat,analogclock,textswitcher,linearlayoutics,appcompatcheckbox,absolutelayout,fitwindowsframelayout}"),
                                     Feature(name="Children2", value=children2, possible_values="{none,item,button,view,framelayout,swiperefreshlayout,imageview,textview,relativelayout,linearlayout,checkbox,scrollview,checkedtextview,edittext,progressbar,recyclerview,space,imagebutton,actionbarcontainer,appcompatimageview,tintimageview,textviewwrapper,pagertabstrip,webview,viewpager,listview,listmenuitemview,radiobutton,appcompattextview,seekbar,ratingbar,expandablelistview,dialogtitle,autocompletetextview,checkableimagebutton,switchcompat,preferenceimageview,actionbarcontextview,navigationview,actionmenuitemview,viewstub,fitwindowslinearlayout,floatingactionbutton,tablelayout,drawerlayout,toolbar,datetimeview,cardview,menu,tablerow,spinner,horizontalscrollview,textinputlayout,appcompatbutton,preferencescreen,surfaceview,viewstubcompat,group,unpressablelinearlayout,buttonbarlayout,nestedscrollview,gridview,navigationmenuview,radiogroup,numberpicker,contentframelayout,switch,gallery,videoview,searchview,actionmenuview,navigationmenuitemview,viewanimator,gridlayout,appcompatradiobutton,chronometer,viewswitcher,checkboxpreference,togglebutton,pagertitlestrip,actionbarview,calendarview,viewflipper,tablayout,appbarlayout,timepicker,slidingdrawer,fitwindowsframelayout,actionbaroverlaylayout,textureview,datepicker,tabwidget,textswitcher,coordinatorlayout,baselinelayout,linearlayoutcompat,imageswitcher,preferencecategory,expandedmenuview,listpreference,appcompatcheckbox,appcompatspinner,preference,tabhost,fragmenttabhost}"),
                                     Feature(name="HasEvent", value="true", possible_values="{false,true}")])

        model.add_test_instance(test_instance)

    @staticmethod
    def classify(data):
        logger = logging.getLogger(ModelBased.__class__.__name__)

        model = Model(classifier_type="trees.RandomForest", verbose=True,
                      classpath='/usr/local/Caskroom/weka/3.9.1/weka-3-9-1/weka.jar')

        for item in data:
                ModelBased.add_instance(model, item)

        try:
            model.test(model_file="resources/HasModel.model")
        except:
            logger.warning("cannot classify %s" % data)
            return []

        return model.predictions

    @staticmethod
    def select(predictions):
        probabilities = []

        for prediction in predictions:
            if prediction.predicted_value == 'false':
                probabilities.append(1.0 - prediction.probability)
            else:
                probabilities.append(prediction.probability)

        if len(probabilities) == 0:
            return -1

        return ModelBased.stochastic_select(probabilities, 10)

    @staticmethod
    def stochastic_select(weight, n_select):
        n = len(weight)
        counter = [0] * n

        for i in range(n_select):
            index = ModelBased.roulette_select(weight)
            counter[index] += 1

        return counter.index(max(counter))

    @staticmethod
    def roulette_select(weight):
        # calculate the total weight
        weight_sum = sum(weight)

        # get a random value
        value = random.random() * weight_sum

        # locate the random value based on the weights
        for i in range(len(weight)):
            value -= weight[i]
            if value <= 0:
                return i

        # when rounding errors occur, we return the last item's index
        return len(weight) - 1



