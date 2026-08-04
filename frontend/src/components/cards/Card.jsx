function Card({ title, icon, children }) {

    return (

        <div className="bg-white rounded-xl shadow-lg p-6 mt-6">

            <h2 className="text-xl font-bold mb-4">

                {icon} {title}

            </h2>

            {children}

        </div>

    );

}

export default Card;