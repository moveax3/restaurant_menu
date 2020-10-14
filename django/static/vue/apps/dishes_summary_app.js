Vue.use(BootstrapVue);

const DishesSummaryTemplate = `
<div class="p-5">
    <h1>Вы выбрали:</h1>
    <div class="row p-5">
        <div
        v-if="dishes"
        v-for="dish in dishes"
        class="col-md-4"
        >
            <h4>{{ dish.name }}</h4>
            <p>Цена: {{ dish.price }} рублей</p>
            <p>Белки: {{ dish.nutritional_value.proteins }} на 100гр.</p>
            <p>Жиры: {{ dish.nutritional_value.fats }} на 100гр.</p>
            <p>Углеводы: {{ dish.nutritional_value.carbohydrates }} на 100гр.</p>
            <p>Калории: {{ dish.nutritional_value.calories }} Кал.</p>
            <img
                :src="dish.picture.picture"
                class="mw-100 mh-300"
            />
        </div>
    </div>
    <h2 class="table-bordered mt-5 mb-2">Аллергены 😱:</h2>
    <p v-for="allergen in allergens">
        {{ allergen }}
    </p>
    <h2 class="table-bordered mt-5 mb-2">Итого: {{total_price()}} рублей.</h2>
</div>
`;


app = new Vue({
    el: '#dishes_summary_app',
    data: {
        dishes: [],
        allergens: [],
    },
    template: DishesSummaryTemplate,
    methods: {
        total_price: function () {
            var price = 0;
            for (dish of this.dishes) {
                price += dish.price;
            }
            return price;
        },
    },
    mounted: function () {
        var that = this;
        var checked_dishes = $cookies.get('checked_dishes');
        var dishes_ids = "";
        for (dish_id of Object.keys(checked_dishes)) {
            if (checked_dishes[dish_id] == true){
                dishes_ids += `${dish_id},`;
            }
        }
        axios.get(`${API_URLS.dishes}?dishes=${dishes_ids}`)
            .then((response) => {
                that.dishes = response.data;
                that.allergens = [];
                for (dish of that.dishes) {
                    for (allergen of dish.allergens) {
                        if (!that.allergens.includes(allergen.name)) {
                            that.allergens.push(allergen.name);
                        }
                    }
                }
            });
    },



});
